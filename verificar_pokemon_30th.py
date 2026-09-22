#!/usr/bin/env python3
"""
Verifica a página de Cartas Pokémon da Centroxogo e avisa (notificação push
via ntfy.sh) sempre que um produto "30th" (Celebration/Anniversary) deixar
de estar "Esgotado".

Pensado para correr no GitHub Actions (ver .github/workflows/check.yml),
mas também corre localmente:
    pip install requests beautifulsoup4
    NTFY_TOPIC="o-teu-topico-secreto" python verificar_pokemon_30th.py
"""

import os
import sys
import requests
from bs4 import BeautifulSoup

URL = "https://www.centroxogo.pt/brinquedos-personagem/pokemon/cartas-pokemon.html"
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "")
NTFY_URL = f"https://ntfy.sh/{NTFY_TOPIC}"


def enviar_notificacao(titulo: str, mensagem: str, link: str = ""):
    if not NTFY_TOPIC:
        print("Aviso: NTFY_TOPIC não definido, notificação não enviada.")
        return
    headers = {"Title": titulo.encode("utf-8"), "Priority": "high"}
    if link:
        headers["Click"] = link
    requests.post(NTFY_URL, data=mensagem.encode("utf-8"), headers=headers, timeout=15)


def verificar():
    resposta = requests.get(
        URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; StockChecker/1.0)"},
        timeout=20,
    )
    resposta.raise_for_status()
    soup = BeautifulSoup(resposta.text, "html.parser")

    disponiveis = []

    for item in soup.select("li.item.product.product-item"):
        nome_tag = item.select_one(".product-item-link")
        if not nome_tag:
            continue
        nome = nome_tag.get_text(strip=True)

        if "30" not in nome:
            continue  # só nos interessam os produtos do 30º aniversário

        texto_item = item.get_text(" ", strip=True).lower()
        esgotado = "esgotado" in texto_item

        if not esgotado:
            link_tag = item.select_one("a")
            link = link_tag["href"] if link_tag else URL
            disponiveis.append((nome, link))

    return disponiveis


def main():
    try:
        disponiveis = verificar()
    except Exception as e:
        print(f"Erro ao verificar a página: {e}")
        sys.exit(1)

    if disponiveis:
        for nome, link in disponiveis:
            print(f"DISPONÍVEL: {nome} -> {link}")
            enviar_notificacao(
                titulo="Pokémon 30th Anniversary disponível!",
                mensagem=nome,
                link=link,
            )
    else:
        print("Nenhum produto 30th disponível de momento.")


if __name__ == "__main__":
    main()

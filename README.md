# Aviso automático: Pokémon TCG 30th Anniversary (Centroxogo)

Isto corre sozinho no GitHub (grátis), a cada 5 minutos (o mínimo possível
no GitHub Actions), e manda-te uma notificação push para o telemóvel assim
que algum produto "30th" deixar de estar Esgotado na Centroxogo.

**Importante:** cria o repositório como "Public", não "Private". A 5 em 5
minutos, um repositório privado esgota os minutos grátis do GitHub a meio
do mês; num repositório público as Actions são grátis e ilimitadas. O teu
tópico ntfy continua protegido, porque fica guardado como "secret" e nunca
aparece no código.

## Passo a passo (uns 5 minutos, só se faz uma vez)

### 1. Instala a app ntfy no telemóvel
- iOS: procura "ntfy" na App Store
- Android: procura "ntfy" na Play Store (ou em ntfy.sh)
- Abre a app → "+" → escreve um nome de tópico só teu e difícil de adivinhar,
  por exemplo: `cat-pokemon-9f2k7` → Subscrever

### 2. Cria uma conta no GitHub (se ainda não tiveres)
https://github.com/signup — é grátis.

### 3. Cria um novo repositório
- No GitHub, clica em "New repository"
- Nome: `pokemon-30th-checker` (ou o que quiseres)
- Escolhe "Public" (ver nota acima sobre minutos grátis)
- Cria o repositório vazio

### 4. Envia estes ficheiros para o repositório
Podes arrastar os 3 ficheiros/pastas diretamente na página do GitHub
("uploading an existing file"), mantendo esta estrutura:

```
pokemon-30th-checker/
├── verificar_pokemon_30th.py
├── .github/
│   └── workflows/
│       └── check.yml
```

(O GitHub deteta automaticamente a pasta `.github/workflows` e ativa as
Actions.)

### 5. Guarda o teu tópico ntfy como "secret"
- No repositório: Settings → Secrets and variables → Actions → "New repository secret"
- Nome: `NTFY_TOPIC`
- Valor: o mesmo nome que usaste na app ntfy (ex: `cat-pokemon-9f2k7`)
- Guardar

### 6. Pronto — testa manualmente
- No repositório: separador "Actions" → escolhe o workflow "Verificar Pokémon 30th Anniversary"
- Clica "Run workflow" para testar já, sem esperar pelos 30 minutos
- Devias ver o resultado no log ("Nenhum produto 30th disponível de momento." se ainda estiver tudo esgotado)

A partir daqui, corre sozinho a cada 30 minutos, e recebes notificação no
telemóvel assim que houver stock de algum produto do 30º aniversário.

## Notas
- Podes mudar a cadência no ficheiro `check.yml` (linha do `cron`).
- É tudo gratuito dentro dos limites normais do GitHub Actions para repositórios pessoais.
- Se a Centroxogo mudar o design da página no futuro, pode ser necessário ajustar o script.

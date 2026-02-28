# 🚀 Deploy no Streamlit Community Cloud (Gratuito)

Como migramos de Chainlit para o **Streamlit**, você não precisa mais se preocupar com Docker, portas ou Render. O Streamlit tem sua própria plataforma de hospedagem gratuita e nativa, focada exatamente no que você está criando.

## 1. Subir para o GitHub

Seu repositório já está no GitHub, então só precisamos garantir que os arquivos novos do Streamlit subam. Execute no terminal:

```bash
git add app_streamlit.py pyproject.toml uv.lock
git commit -m "Migração para Streamlit"
git push origin main
```

## 2. Fazer Deploy no Streamlit Cloud

1. Acesse [share.streamlit.io](https://share.streamlit.io) e faça login conectando sua conta do GitHub.
2. Clique em **"New app"**.
3. Escolha a opção **"Use existing repo"**.
4. Preencha:
   - **Repository:** `leoserpa/agno-seo-project` (o seu repositório)
   - **Branch:** `main`
   - **Main file path:** `app_streamlit.py`
5. Antes de clicar me "Deploy", clique em **"Advanced settings"** (no canto inferior).

## 3. Configurar Variáveis de Ambiente (Secrets)

Dentro de **Advanced settings**, há uma caixa de texto chamada "Secrets". É lá que você coloca suas chaves de API (exatamente como estavam no `.env`):

```toml
GOOGLE_API_KEY="AIzaSy..."
GROQ_API_KEY="gsk_..."
```

> **Aviso:** O Streamlit aceita o formato `.toml` (com aspas nos valores) direto na nuvem.

6. Clique em **"Save"**.
7. Por fim, clique no botão **"Deploy!"**.

O Streamlit vai ler seu `pyproject.toml` (graças ao suporte nativo a UV que ele tem) e em cerca de 2 minutos seu app estará no ar com uma URL bonitinha como `https://sua-agencia.streamlit.app`!

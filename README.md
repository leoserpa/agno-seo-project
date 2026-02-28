---
title: Agencia de Marketing IA
emoji: 🚀
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
app_port: 7860
---

# 🚀 Agência de Marketing Digital com IA

Assistente inteligente com **5 agentes especializados** em marketing digital e SEO, construído com [Agno](https://agno.com) e [Chainlit](https://chainlit.io).

## 💼 Agentes Disponíveis

| Agente | Descrição |
|--------|-----------|
| 📅 **Estrategista** | Cria calendários e cronogramas de conteúdo |
| ✍️ **Agente SEO** | Escreve artigos otimizados para buscadores |
| 🔍 **Revisor SEO** | Avalia e pontua artigos antes da publicação |
| 📱 **Adaptador Social** | Gera posts para Instagram, Facebook, LinkedIn e X |
| 📧 **Gerador de Email** | Cria newsletters e campanhas de email marketing |

## 🛠️ Tecnologias

- **Framework de Agentes**: [Agno](https://agno.com)
- **Interface**: [Chainlit](https://chainlit.io)
- **LLMs**: Google Gemini + Groq
- **Busca na Web**: DuckDuckGo Search

## 🚀 Como Usar

Digite o que seu negócio precisa diretamente no chat. Exemplos:

- *"Cria um calendário de conteúdo para uma loja de roupas para Março"*
- *"Escreve um artigo SEO sobre marketing digital em 2026"*
- *"Adapta esse artigo para Instagram"*
- *"Avalia o SEO desse texto: ..."*

## ⚙️ Configuração Local

```bash
# Clone o repositório
git clone https://huggingface.co/spaces/SEU-USUARIO/agencia-marketing-ia
cd agencia-marketing-ia

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas chaves de API

# Instale as dependências
pip install -r requirements-deploy.txt

# Inicie o servidor
chainlit run app_chainlit.py
```

## 🔑 Variáveis de Ambiente Necessárias

Configure em **Settings → Variables and secrets** no Hugging Face Space:

| Variável | Descrição |
|----------|-----------|
| `GOOGLE_API_KEY` | Chave da API do Google Gemini |
| `GROQ_API_KEY` | Chave da API do Groq |

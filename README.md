# 🤖 Agência de Marketing Digital com IA

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agno-marketing-ai-akm3k8ohwvnzfruzcusbj8.streamlit.app/)

Assistente inteligente e autônomo com **5 agentes especializados** em Marketing Digital e SEO, construído com o poderoso framework **[Agno](https://agno.com)** e interface moderna em **[Streamlit](https://streamlit.io)**.

## 💼 A Equipe de Agentes

O projeto utiliza um Orquestrador (Team Leader) que analisa seu pedido e roteia para o especialista adequado:

| Agente | Especialidade | Descrição |
|--------|---------------|-----------|
| 📅 **Estrategista** | Planejamento | Cria calendários e cronogramas de conteúdo detalhados |
| ✍️ **Agente SEO** | Redação | Escreve artigos longos otimizados para motores de busca |
| 🔍 **Revisor SEO** | Auditoria | Avalia, pontua e sugere melhorias em artigos antes da publicação |
| 📱 **Adaptador Social**| Redes Sociais | Gera posts virais adaptados para Instagram, LinkedIn e X |
| 📧 **Gerador de Email** | Conversão | Cria newsletters e campanhas de email marketing persuasivas |

## ✨ Destaques & Funcionalidades (UI/UX)
- ⚡ **Respostas em Streaming ao Vivo:** O texto é digitado na tela de forma contínua igual ao ChatGPT, sem travamentos.
- 🎯 **Atalhos de Ação Rápida:** Tela inicial com botões para gerar artigos, posts e calendários com 1 clique.
- 🧹 **Sidebar Funcional:** Painel lateral elegante com a opção de Limpar Conversa e resetar a memória do agente.
- 🧠 **Busca na Web em Tempo Real:** Conectado ao DuckDuckGo para recuperar informações atualizadas e notícias recentes.

## 🛠️ Tecnologias Utilizadas

- **Framework de IA:** [Agno](https://agno.com) (Ex-Phidata)
- **Interface Gráfica Web:** [Streamlit](https://streamlit.io)
- **Modelos de Linguagem (LLMs):** Google Gemini 2.5 Flash / Groq
- **Gerenciador de Pacotes:** uv (Extremamente rápido)

## 🚀 Como Rodar Localmente

Se quiser rodar os agentes no seu próprio computador:

1. **Clone o repositório:**
```bash
git clone https://github.com/SEU-USUARIO/agno-seo-agent.git
cd agno-seo-agent
```

2. **Configure suas Chaves de API:**
Crie um arquivo `.env` na raiz do projeto contendo as chaves dos modelos que desejar utilizar (Google, Groq, OpenAI ou Anthropic):
```env
# Chaves Principais (Atuais)
GOOGLE_API_KEY=sua_chave_do_google_aqui
GROQ_API_KEY=sua_chave_do_groq_aqui

# Outras opções suportadas pelo Agno (Opcionais)
OPENAI_API_KEY=sua_chave_da_openai_aqui
ANTHROPIC_API_KEY=sua_chave_da_anthropic_claude_aqui
```

3. **Inicie a Interface:**
Usando o `uv` (recomendado) ou pip tradicional:
```bash
uv run streamlit run app_streamlit.py
```
*O painel abrirá automaticamente no seu navegador em `http://localhost:8501/`*

## 🌐 Deploy na Nuvem (Streamlit Cloud)

Este projeto está configurado para deploy imediato no **Streamlit Community Cloud** de forma 100% gratuita.

1. Acesse [share.streamlit.io](https://share.streamlit.io/).
2. Conecte com seu GitHub e clique em **New App**.
3. Selecione este repositório e o arquivo principal: `app_streamlit.py`.
4. Em **Advanced Settings**, cole o conteúdo do seu `.env` na caixa de **Secrets** usando o padrão TOML:
```toml
GOOGLE_API_KEY="sua_chave_aqui"
GROQ_API_KEY="sua_chave_aqui"
```
5. Clique em **Deploy**!

## 📜 Licença

Este projeto é desenvolvido sob a **Licença MIT** (MIT License). Você tem permissão para usar, copiar, modificar, e distribuir este software de forma gratuita para fins pessoais ou comerciais, desde que o aviso de direitos autorais seja mantido. Veja o arquivo `LICENSE` para mais detalhes.

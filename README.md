# 🤖 Agência de Marketing Digital com IA

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agno-marketing-ai-akm3k8ohwvnzfruzcusbj8.streamlit.app/)

Assistente inteligente e autônomo com **5 agentes especializados** em Marketing Digital e SEO, construído com o poderoso framework **[Agno](https://agno.com)** e interface moderna em **[Streamlit](https://streamlit.io)**.

<div align="center">
  <img src="assets/img1.png" alt="Tela Principal da Agência IA" width="48%">
  <img src="assets/img2.png" alt="Chat e Execução dos Agentes" width="48%">
</div>

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
- **Modelo de Linguagem (LLMs):** Google Gemini 2.5 Flash 
- **Gerenciador de Pacotes:** uv (Extremamente rápido)

## 💡 Exemplos de Prompts para o Chat

Você pode interagir livremente com a agência. Aqui estão alguns exemplos testados para extrair o máximo do orquestrador ou de agentes individuais:

- 🤖 **Orquestrador Central (Planejamento)**
  > *"Acabei de lançar uma clínica odontológica. Monte um calendário de ideias para 3 posts no Instagram focados em captação de clientes. Avalie a melhor estratégia."*

- 🔍 **Agente Redator SEO**
  > *"Escreva um artigo de blog sobre as 5 principais tendências de design de interiores. Otimize a meta description e use a palavra-chave 'arquitetura moderna' ao longo do texto."*

- �️ **Agente Revisor SEO**
  > *"Analise o artigo abaixo e me dê uma nota de 0 a 100 para SEO. Sugira melhorias na densidade de palavras-chave e verifique se o tom de voz está persuasivo. [cole o texto aqui]"*

- �📱 **Agente de Redes Sociais**
  > *"Crie um roteiro para um Reels do Instagram dando três dicas essenciais para iniciantes começarem a investir. Finalize com uma chamada para ação (CTA) para o link da bio."*

- 📧 **Agente de Email Marketing**
  > *"Escreva um email persuasivo de remarketing para clientes que abandonaram o carrinho comprando um tênis de corrida na minha loja. Ofereça 10% de desconto no assunto do email."*

## 🚀 Como Rodar Localmente

Se quiser rodar os agentes no seu próprio computador:

1. **Clone o repositório:**
```bash
git clone https://github.com/leoserpa/agno-marketing-ai.git
cd agno-marketing-ai
```

2. **Configure suas Chaves de API:**
Crie um arquivo `.env` na raiz do projeto contendo as chaves dos modelos que desejar utilizar (Google, Groq, OpenAI ou Anthropic):
```env
# Chaves Principais (Atuais)
GOOGLE_API_KEY=sua_chave_do_google_aqui
GROQ_API_KEY=sua_chave_do_groq_aqui
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
# Chaves Principais
GOOGLE_API_KEY="sua_chave_aqui"
GROQ_API_KEY="sua_chave_aqui"
OPENAI_API_KEY="sua_chave_aqui"
ANTHROPIC_API_KEY="sua_chave_aqui"
```
5. Clique em **Deploy**!

## ⚠️ Cota e Uso de API

A infraestrutura dos agentes neste software está pré-configurada para rodar usando a camada gratuita (*Free Tier*) do modelo **Google Gemini 2.5 Flash**. 
Se ocorrerem instabilidades no servidor ou o limite diário da conta for atingido, os agentes exibirão um aviso vermelho na tela. Recomendamos conectar a sua própria Chave de API (Google, OpenAI, Anthropic ou Groq) no arquivo `.env` (ou no painel Secrets do deploy) para aumentar o volume de operações do seu uso diário.

## 📜 Licença

Este projeto é desenvolvido sob a **Licença MIT** (MIT License). Você tem permissão para usar, copiar, modificar, e distribuir este software de forma gratuita para fins pessoais ou comerciais, desde que o aviso de direitos autorais seja mantido. Veja o arquivo `LICENSE` para mais detalhes.

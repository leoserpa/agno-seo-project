# 🤖 Sistema Multi-Agente de SEO e Marketing Digital

Sistema de IA com **5 agentes especializados + 1 orquestrador** para criação de conteúdo SEO, construído com o framework [Agno](https://agno.com).

## 🏗️ Arquitetura

```
                    💬 Assistente de SEO (Orquestrador)
                              ↓ roteia
          ┌───────────┬───────────┬───────────┬───────────┐
          ↓           ↓           ↓           ↓           ↓
     📅 Estrateg.  ✍️ Escritor  🔍 Revisor  📱 Social  📧 Email
```

| Agente | Arquivo | Função |
|---|---|---|
| � Estrategista | `estrategista.py` | Cria calendários de conteúdo |
| ✍️ Escritor SEO | `agente.py` | Escreve artigos otimizados |
| 🔍 Revisor SEO | `revisor_seo.py` | Avalia artigos (nota 0-100) |
| 📱 Adaptador Social | `adaptador_social.py` | Posts para Instagram, Facebook, LinkedIn e X |
| 📧 Gerador de Email | `gerador_email.py` | Newsletters e emails de vendas |
| 🤖 Assistente de SEO | `orquestrador.py` | Direciona para o agente certo automaticamente |

## ⚡ Funcionalidades

- ✅ **5 agentes especializados** com guardas de escopo
- ✅ **Orquestrador inteligente** (mode=route) — 1 ponto de entrada
- ✅ **Análise de keywords** interativa (apresenta antes de escrever)
- ✅ **Tom personalizável** — formal, casual ou técnico
- ✅ **Pesquisa web em tempo real** via DuckDuckGo
- ✅ **Memória de conversa** — lembra das últimas interações
- ✅ **Storage SQLite** — sessões persistentes
- ✅ **Playground web** via AgentOS

## 🛠️ Stack

- **Framework:** [Agno](https://agno.com) (Python)
- **Modelo:** Groq Llama 3.3 70B (gratuito)
- **Pesquisa:** DuckDuckGo
- **Storage:** SQLite
- **Interface:** AgentOS Playground / Streamlit (em breve)

## 🚀 Como Usar

### 1. Clonar e instalar

```bash
git clone https://github.com/leoserpa/agno-seo-project.git
cd agno-seo-project
uv sync
```

### 2. Configurar API Keys

Crie um arquivo `.env` na raiz:

```
GROQ_API_KEY=sua_chave_do_groq
GOOGLE_API_KEY=sua_chave_do_google (opcional)
```

Obtenha grátis em: [console.groq.com](https://console.groq.com)

### 3. Iniciar o servidor

```bash
uv run python agent_os.py
```

### 4. Acessar o Playground

Acesse [os.agno.com](https://os.agno.com) e conecte em `localhost:7777`.

## 📁 Estrutura do Projeto

```
├── agente.py            # ✍️ Agente Escritor SEO
├── revisor_seo.py       # 🔍 Agente Revisor (nota 0-100)
├── adaptador_social.py  # 📱 Adaptador de Redes Sociais
├── gerador_email.py     # 📧 Gerador de Email Marketing
├── estrategista.py      # 📅 Estrategista de Conteúdo
├── orquestrador.py      # 🤖 Orquestrador (Team route)
├── agent_os.py          # 🖥️ Servidor AgentOS
├── main.py              # 🧪 Teste rápido no terminal
├── .env                 # 🔑 API keys (não versionado)
└── pyproject.toml       # 📦 Dependências
```

## 📝 Exemplos de Uso

**Escrever artigo:**
> "Escreva um artigo sobre SEO para e-commerce, tom casual"

**Revisar artigo:**
> Cole o artigo e peça: "Avalie esse artigo"

**Criar posts:**
> "Crie posts sobre SEO local para redes sociais"

**Criar email:**
> "Crie uma newsletter sobre tendências de SEO 2026"

**Planejar conteúdo:**
> "Crie um calendário de conteúdo para uma agência de marketing"

## 📄 Licença

MIT

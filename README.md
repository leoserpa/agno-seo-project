# 🤖 Agente Escritor de SEO com Agno

Agente de IA que escreve artigos otimizados para SEO, com pesquisa em tempo real e formatação Markdown profissional.

> 🚧 **Status: Em desenvolvimento** — O agente funciona, mas novas funcionalidades estão sendo adicionadas.

## Stack

- **Framework:** [Agno](https://agno.com) (Python)
- **Modelo:** Gemini 2.5 Flash (Google AI Studio — gratuito)
- **Pesquisa Web:** DuckDuckGo (via `DuckDuckGoTools`)
- **Output:** Markdown pronto para WordPress / Ghost

## Funcionalidades

- ✅ Pesquisa web em tempo real antes de escrever
- ✅ Persona de Redator SEO com 10 anos de experiência
- ✅ Estrutura SEO: H1/H2/H3, palavras-chave, meta description
- ✅ Output Markdown com frontmatter YAML, conclusão e FAQ
- ✅ Custo zero (tier gratuito do Gemini)

## Como Usar

### 1. Instalar dependências

```bash
uv sync
```

### 2. Configurar API Key

Cria um ficheiro `.env` na raiz do projeto:

```
GOOGLE_API_KEY=a_tua_chave_do_google_ai_studio
```

Obtém a chave em: [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 3. Executar

```bash
uv run python main.py
```

## Estrutura

```
├── main.py          # Agente SEO principal
├── .env             # API keys (não versionado)
├── .gitignore       # Exclui .env e .venv
├── pyproject.toml   # Dependências do projeto
└── README.md        # Este ficheiro
```

## Roadmap

- [ ] Receber o tema do artigo como argumento CLI
- [ ] Salvar artigos gerados em ficheiros `.md`
- [ ] Interface web com Agno Playground
- [ ] Suporte a múltiplos idiomas

## Licença

MIT

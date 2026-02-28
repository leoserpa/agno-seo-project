# ============================================================
# DOCKERFILE — Deploy no Render / Hugging Face Spaces
# ============================================================

# 1. BASE: Python 3.13 slim
FROM python:3.13-slim

# 2. INSTALAR UV (gerenciador de pacotes rápido)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. SEGURANÇA: usuário não-root (obrigatório no HF Spaces)
RUN useradd -m -u 1000 user
USER user

# 4. PASTA DE TRABALHO
WORKDIR /app

# 5. COPIAR ARQUIVOS DE DEPENDÊNCIAS
COPY --chown=user pyproject.toml uv.lock ./

# 6. INSTALAR DEPENDÊNCIAS COM UV SYNC (método oficial)
# Isso criará um ambiente virtual em /app/.venv
RUN uv sync --frozen --no-install-project

# 7. ADICIONAR O VENV AO PATH
# Assim o sistema acha o chainlit e python dentro do .venv criado pelo uv
ENV PATH="/app/.venv/bin:$PATH"

# 8. COPIAR O CÓDIGO FONTE
COPY --chown=user . .

# 9. EXPOR A PORTA
EXPOSE 7860

# 10. INICIAR O CHAINLIT
# Usa shell form para garantir que $PORT (do Render) seja resolvido
CMD chainlit run app_chainlit.py --host 0.0.0.0 --port ${PORT:-7860}

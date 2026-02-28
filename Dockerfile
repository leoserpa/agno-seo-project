# ============================================================
# DOCKERFILE — Deploy no Render / Hugging Face Spaces
# Usa UV como gerenciador de pacotes (mais rápido que pip)
# ============================================================

# 1. BASE: Python 3.13 slim
FROM python:3.13-slim

# 2. INSTALAR UV (gerenciador de pacotes do projeto)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. SEGURANÇA: usuário não-root
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 4. PASTA DE TRABALHO
WORKDIR /app

# 5. COPIAR ARQUIVOS DE DEPENDÊNCIAS PRIMEIRO (cache do Docker)
COPY --chown=user pyproject.toml uv.lock ./

# 6. INSTALAR DEPENDÊNCIAS COM UV
# --system: instala no Python do sistema (sem venv, ideal para Docker)
# --frozen: usa versões exatas do uv.lock (reproduzível)
RUN uv pip install --system --no-cache -r pyproject.toml

# 7. COPIAR O CÓDIGO FONTE
COPY --chown=user . .

# 8. EXPOR PORTA (informativo)
EXPOSE 7860

# 9. INICIAR O CHAINLIT
# ${PORT:-7860}: usa $PORT (Render) ou 7860 (HF Spaces) como fallback
CMD chainlit run app_chainlit.py --host 0.0.0.0 --port ${PORT:-7860}

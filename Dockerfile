# ============================================================
# DOCKERFILE — Deploy no Render / Hugging Face Spaces
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

# 5. COPIAR ARQUIVOS DO PROJETO
COPY --chown=user . .

# 6. INSTALAR DEPENDÊNCIAS COM UV
# "uv pip install --system ." lê o pyproject.toml e instala tudo
RUN uv pip install --system --no-cache .

# 7. EXPOR PORTA (informativo)
EXPOSE 7860

# 8. INICIAR O CHAINLIT
# ${PORT:-7860}: usa $PORT (Render) ou 7860 (HF Spaces) como fallback
CMD chainlit run app_chainlit.py --host 0.0.0.0 --port ${PORT:-7860}

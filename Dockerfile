# ============================================================
# DOCKERFILE — Deploy no Render / Hugging Face Spaces
# ============================================================
# Render: injeta a porta via variável $PORT automaticamente
# Hugging Face: usa sempre a porta 7860
# ${PORT:-7860} = usa $PORT se existir, senão usa 7860
# ============================================================

# 1. BASE: Python 3.13 slim (compatível com pyproject.toml)
FROM python:3.13-slim

# 2. SEGURANÇA: usuário não-root (boas práticas e obrigatório no HF)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 3. PASTA DE TRABALHO
WORKDIR /app

# 4. INSTALAR DEPENDÊNCIAS
COPY --chown=user pyproject.toml .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    "agno>=2.5.5" \
    "chainlit>=2.9.6" \
    "ddgs>=9.10.0" \
    "fastapi>=0.133.1" \
    "google-genai>=1.65.0" \
    "groq>=1.0.0" \
    "python-dotenv>=1.2.1" \
    "uvicorn>=0.41.0"

# 5. COPIAR O CÓDIGO FONTE
COPY --chown=user . .

# 6. EXPOR PORTA (informativo)
EXPOSE 7860

# 7. INICIAR O CHAINLIT
# Usa shell form para permitir expansão de variável ${PORT:-7860}
# Render define $PORT automaticamente; HF Spaces usa 7860 por padrão
CMD chainlit run app_chainlit.py --host 0.0.0.0 --port ${PORT:-7860}

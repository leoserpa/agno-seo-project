# 1. ESCOLHENDO A BASE (O SISTEMA OPERACIONAL)
# Pense nisso como comprar um computador novo. Estamos escolhendo um "computador" 
# que já vem com o Python 3.11 instalado. A palavra "slim" significa que ele é 
# magrinho, sem programas inúteis, para nossa aplicação ficar leve e rápida.
FROM python:3.11-slim

# 2. CRIANDO UM USUÁRIO COMUM (SEGURANÇA)
# Por padrão, o Docker roda como "Administrador" (root). 
# O Hugging Face nos obriga, por segurança, a criar um usuário comum chamado "user"
# e dar permissão de instalar programas apenas para ele.
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# 3. DEFININDO A PASTA DE TRABALHO
# O comando WORKDIR diz: "A partir de agora, tudo que formos fazer neste 
# computador virtual será dentro da pasta /app".
WORKDIR /app

# 4. INSTALANDO AS DEPENDÊNCIAS (BIBLIOTECAS)
# Primeiro copiamos apenas o requirements.txt do seu PC para o computador virtual.
# Depois rodamos "pip install" nele. Fazemos isso separado do resto dos arquivos
# para que o Docker não precise reinstalar tudo se você apenas mudar um texto no código.
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. COPIANDO O NOSSO CÓDIGO FONTE
# Agora sim copiamos todos os arquivos da sua pasta (orquestrador.py, agente.py, etc) 
# para dentro do computador virtual (pasta /app).
COPY --chown=user . .

# 6. ABRINDO A PORTA DE COMUNICAÇÃO
# Nosso Chainlit vai rodar dentro deste computador virtual, mas precisamos abrir uma 
# "porta" para a internet enxergar a tela dele. O Hugging Face obriga que seja a 7860.
EXPOSE 7860

# 7. O COMANDO FINAL (LIGANDO TUDO)
# É o equivalente a você digitar "uv run chainlit run app_chainlit.py" no seu terminal.
# Quando a máquina virtual ligar de fato na nuvem, este será o primeiro e único comando 
# que ela vai executar lá dentro para subir o site.
CMD ["chainlit", "run", "app_chainlit.py", "--host", "0.0.0.0", "--port", "7860"]

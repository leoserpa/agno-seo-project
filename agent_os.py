"""Servidor AgentOS — Serve os Agentes SEO com Playground.

Rastreamento de Execução:
    1. Importa os 3 agentes: Escritor, Revisor e Adaptador Social
    2. Cria o AgentOS com os 2 agentes + storage + tracing
    3. Gera a app FastAPI (servidor web)
    4. Inicia na porta 7777 — acessível pelo Playground em os.agno.com
"""

from agno.os import AgentOS
from agente import agente_seo, db
from revisor_seo import revisor_seo
from adaptador_social import adaptador_social


# ============================================================
# PASSO 1: Criar o AgentOS
# ============================================================
# O AgentOS transforma o agente Python num servidor web.
# Isso permite que o Playground (os.agno.com) se conecte a ele.
agent_os = AgentOS(
    # Nome do sistema (aparece no Playground)
    name="SEO Writer OS",

    # Lista de agentes disponíveis - (podemos ter vários - temos 3)
    # No Playground, o utilizador escolhe qual quer usar
    agents=[agente_seo, revisor_seo, adaptador_social],

    # Conecta o storage SQLite — guarda logs e sessões do Playground
    db=db,

    # Ativa o rastreamento: registra cada interação (quem perguntou, o que respondeu)
    tracing=True,
)


# ============================================================
# PASSO 2: Criar a App FastAPI
# ============================================================
# O AgentOS gera automaticamente um servidor web FastAPI com:
#   - Rota /agents → lista os agentes disponíveis
#   - Rota /chat → envia mensagens para o agente
#   - Rota /sessions → lista sessões guardadas
app = agent_os.get_app()


# ============================================================
# PASSO 3: Iniciar o Servidor
# ============================================================
if __name__ == "__main__":
    try:
        # Inicia o servidor Uvicorn na porta 7777
        # reload=True → reinicia quando editas o código (modo desenvolvimento)
        agent_os.serve(app="agent_os:app", reload=True)
    except KeyboardInterrupt:
        # Ctrl+C no terminal encerra o servidor de forma limpa
        print("\n👋 Servidor encerrado.")
    except OSError as e:
        # Acontece quando a porta 7777 já está ocupada por outro programa
        print(f"❌ Erro: {e}")
        print("💡 Fecha o outro programa que usa a porta 7777 e tenta de novo.")

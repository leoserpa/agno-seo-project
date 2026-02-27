"""Orquestrador SEO — Recepcionista inteligente que direciona para o agente certo.

Rastreamento de Execução:
    1. Recebe a mensagem do usuário
    2. Analisa o que o usuário quer (escrever? revisar? posts? email? planejar?)
    3. Encaminha para o agente especialista correto
    4. Retorna a resposta do agente escolhido

O que entra: Qualquer pedido relacionado a SEO/Marketing
O que sai: A resposta do agente mais adequado

ONDE ESTE CÓDIGO FICA:
    - Este arquivo cria o "Team" (equipe) com mode="route"
    - O "route" significa: o líder ESCOLHE qual agente usar
    - Só UM agente é chamado por vez (econômico!)
"""

# ============================================================
# IMPORTAÇÕES
# ============================================================
# Team = classe do Agno que agrupa vários agentes numa equipe
from agno.team import Team

# TeamMode = enum que define o modo de funcionamento da equipe
from agno.team.mode import TeamMode

# Groq = modelo de IA que o líder usa para DECIDIR qual agente chamar
from agno.models.groq import Groq

# Importa os 5 agentes que foi criado
from agente import agente_seo          # ✍️ Escreve artigos
from revisor_seo import revisor_seo    # 🔍 Avalia artigos
from adaptador_social import adaptador_social  # 📱 Posts para redes
from gerador_email import gerador_email        # 📧 Emails/newsletters
from estrategista import estrategista          # 📅 Calendário de conteúdo

from agno.db.sqlite import SqliteDb
from dotenv import load_dotenv

load_dotenv()

db_orquestrador = SqliteDb(
    db_file="agent_sessions.db",
    session_table="sessions_orquestrador",
)

# ============================================================
# ORQUESTRADOR (TEAM MODE=ROUTE)
# ============================================================
# Como funciona:
# 1. O usuário fala com o Orquestrador (1 ponto de entrada)
# 2. O modelo do Orquestrador lê a mensagem
# 3. Decide qual dos 5 agentes é o melhor para responder
# 4. Encaminha a mensagem para esse agente
# 5. Retorna a resposta direto (sem modificar)
#
# Exemplo:
#   "Escreve um artigo sobre SEO" → encaminha para ✍️ Escritor
#   "Avalia esse artigo" → encaminha para 🔍 Revisor
#   "Cria posts para Instagram" → encaminha para 📱 Adaptador
#   "Cria uma newsletter" → encaminha para 📧 Email
#   "Planeja conteúdo para o mês" → encaminha para 📅 Estrategista

orquestrador = Team(
    # Nome que aparece no Playground
    name="Assistente de SEO",

    # MODE = ROUTE: escolhe 1 agente por pedido (econômico!)
    # Outros modos: TeamMode.coordinate (chama todos), TeamMode.broadcast (envia para todos)
    mode=TeamMode.route,

    # Modelo que o LÍDER usa para decidir qual agente chamar
    # (é uma chamada rápida e barata, só para decidir)
    model=Groq(id="llama-3.3-70b-versatile"),

    # Os 5 agentes que o Orquestrador pode chamar
    members=[
        estrategista,       # 📅 Planejamento
        agente_seo,         # ✍️ Escrita
        revisor_seo,        # 🔍 Revisão
        adaptador_social,   # 📱 Redes Sociais
        gerador_email,      # 📧 Email Marketing
    ],

    # Instruções para o LÍDER (não para os agentes)
    # Isso ajuda ele a decidir qual agente encaminhar
    instructions=[
        # GUARDA DE ESCOPO — VERIFICAR ANTES DE ROTEAR
        "PRIORIDADE MÁXIMA: ANTES de encaminhar para qualquer agente, verifique "
        "se o pedido é sobre SEO, Marketing Digital ou Criação de Conteúdo. "
        "Se NÃO for, NUNCA encaminhe para nenhum agente. Responda você mesmo "
        "APENAS com: '🚫 Nossa equipe é especializada apenas em SEO e Marketing "
        "Digital. Quer ajuda com alguma estratégia de conteúdo?'",
        "NUNCA encaminhe perguntas sobre: política, presidentes, esporte, culinária, "
        "saúde, programação, matemática, história geral ou qualquer tema fora de SEO.",

        "Você é o Assistente de SEO e Marketing Digital.",
        "Analise o pedido do usuário e encaminhe para o agente correto:\n"
        "- Pedidos de PLANEJAMENTO ou CALENDÁRIO → Estrategista de Conteúdo\n"
        "- Pedidos de ESCRITA de artigos → Agente SEO\n"
        "- Pedidos de REVISÃO ou AVALIAÇÃO → Revisor SEO\n"
        "- Pedidos de POSTS para redes sociais → Adaptador Social\n"
        "- Pedidos de EMAIL ou NEWSLETTER → Gerador de Email",
        "Se o usuário enviar uma saudação, responda: 'Olá! 👋 Sou seu Assistente de SEO. "
        "Posso ajudar com:\n"
        "📅 Planejar seu conteúdo\n"
        "✍️ Escrever artigos otimizados\n"
        "🔍 Avaliar qualidade de SEO\n"
        "📱 Criar posts para redes sociais\n"
        "📧 Criar newsletters e emails\n\n"
        "O que você precisa hoje?'",
        "Escreva em Português do Brasil.",
    ],

    markdown=True,

    # Storage para guardar sessões do orquestrador
    db=db_orquestrador,
    add_history_to_context=True,
    num_history_runs=5,
)

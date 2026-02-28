"""Interface Chainlit — Chat tipo ChatGPT para o Assistente de SEO.

Rastreamento de Execução:
    1. Quando o usuário abre o chat, o @cl.on_chat_start inicializa o orquestrador
    2. Quando o usuário envia uma mensagem, o @cl.on_message processa
    3. O orquestrador decide qual agente usar e retorna a resposta
    4. A resposta aparece no chat com streaming (letra por letra)

COMO FUNCIONA O CHAINLIT:
    - O Chainlit é um framework que cria uma interface de chat bonita
    - Ele usa "decorators" (@cl) para definir o que acontece em cada evento
    - @cl.on_chat_start = quando o chat começa (1 vez)
    - @cl.on_message = quando o usuário envia uma mensagem (toda vez)

COMO RODAR:
    chainlit run app_chainlit.py
"""

import chainlit as cl
import uuid  # Gera IDs únicos para cada sessão de chat
from orquestrador import orquestrador


# ============================================================
# EVENTO: QUANDO O CHAT COMEÇA
# ============================================================
# Isso roda UMA VEZ quando o usuário abre a página.
# Criamos um session_id único para que o agente lembre do histórico.
@cl.on_chat_start
async def on_chat_start():
    """Envia mensagem de boas-vindas e cria sessão."""
    # Gera um ID único para esta conversa
    # Isso permite que o agente lembre das mensagens apenas NAQUELA aba/sessão
    session_id = str(uuid.uuid4())
    cl.user_session.set("session_id", session_id)

    await cl.Message(
        content=(
            "## 👋 Olá! Sou seu Assistente de Marketing Digital\n\n"
            "Posso ajudar com:\n\n"
            "📅 **Planejar** seu conteúdo\n\n"
            "✍️ **Escrever** artigos otimizados para SEO\n\n"
            "🔍 **Avaliar** a qualidade de SEO de um artigo\n\n"
            "📱 **Criar posts** para Instagram, Facebook, LinkedIn e X\n\n"
            "📧 **Criar emails** e newsletters\n\n"
            "---\n\n"
            "**O que você precisa hoje?** 😊"
        )
    ).send()


# ============================================================
# EVENTO: QUANDO O USUÁRIO ENVIA UMA MENSAGEM
# ============================================================
# Isso roda TODA VEZ que o usuário envia algo.
# Usa o session_id para manter o histórico da conversa.
@cl.on_message
async def on_message(message: cl.Message):
    """Processa cada mensagem do usuário e responde via orquestrador."""

    # Pega o session_id que foi criado quando o chat começou
    session_id = cl.user_session.get("session_id")

    # Mostra "pensando..." enquanto o agente processa
    msg = cl.Message(content="")
    await msg.send()

    try:
        # Envia a mensagem para o orquestrador COM o session_id
        # Isso faz o agente lembrar das mensagens anteriores!
        response = orquestrador.run(message.content, session_id=session_id)

        # Extrai o texto da resposta
        # response.content pode ser uma string ou um objeto
        if hasattr(response, "content"):
            response_text = response.content
        else:
            response_text = str(response)

        # Atualiza a mensagem com a resposta do agente
        msg.content = response_text
        await msg.update()

    except Exception as e:
        # Se der erro, mostra uma mensagem amigável
        msg.content = f"⚠️ Ocorreu um erro: {str(e)}\n\nTente novamente!"
        await msg.update()

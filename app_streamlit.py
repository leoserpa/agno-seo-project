"""
Interface Streamlit — Chat tipo ChatGPT para o Assistente de SEO.

COMO FUNCIONA O STREAMLIT:
    Diferente do Chainlit (que roda baseado em eventos), o Streamlit 
    roda o código inteiro de cima para baixo toda vez que o usuário interage.
    
    Por isso, usamos o `st.session_state` para "lembrar" das coisas 
    (como o histórico do chat ou o ID da sessão) entre cada recarregamento da página.

COMO RODAR:
    uv run streamlit run app_streamlit.py
"""

import streamlit as st
import uuid
from orquestrador import orquestrador

# ============================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ============================================================
# Define o título da aba do navegador e o ícone
st.set_page_config(
    page_title="Agência Marketing IA",
    page_icon="🤖",
    layout="centered"
)

# Título principal da página
st.title("🤖 Assistente de Marketing Digital IA")
st.markdown("---")


# ============================================================
# 2. INICIALIZAÇÃO DO ESTADO DA SESSÃO (Memória do App)
# ============================================================

# Se for a primeira vez que o usuário abre a página, cria um ID único para a sessão
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Cria uma lista vazia para guardar o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "## 👋 Olá! Sou seu Assistente de Marketing Digital\n\n"
                "Posso ajudar com:\n"
                "- 📅 **Planejar** seu conteúdo\n"
                "- ✍️ **Escrever** artigos otimizados para SEO\n"
                "- 🔍 **Avaliar** a qualidade de SEO de um artigo\n"
                "- 📱 **Criar posts** para Redes Sociais\n"
                "- 📧 **Criar emails** e newsletters\n\n"
                "**O que você precisa hoje?** 😊"
            )
        }
    ]


# ============================================================
# 3. DESENHAR O HISTÓRICO DE MENSAGENS NA TELA
# ============================================================
# Toda vez que a página recarregar, nós varremos a lista de mensagens salvas
# e desenhamos na tela novamente (balões de chat)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# 4. CAPTURAR A NOVA MENSAGEM DO USUÁRIO
# ============================================================
# A caixa de texto no rodapé da página. Se o usuário digitar algo:
if prompt := st.chat_input("Digite aqui o que você precisa..."):
    
    # PASSO A: Mostrar a mensagem do usuário na tela e salvar na memória
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # PASSO B: Enviar para o Orquestrador (Agno) e esperar a resposta
    with st.chat_message("assistant"):
        # Um "spinner" gira só até a primeira palavra chegar
        with st.spinner("Pensando e pesquisando... ⏳"):
            try:
                # O orquestrador retorna um gerador quando stream=True
                stream_response = orquestrador.run(
                    prompt, 
                    session_id=st.session_state.session_id,
                    stream=True
                )
                
                # Resposta final completa para guardar na memória depois
                resposta_completa = ""
                
                # Container vazio que vamos atualizando letra por letra
                placeholder = st.empty()
                
                for chunk in stream_response:
                    # Em modo Team com stream=True, o Agno frequentemente 
                    # emite a mensagem CONSOLIDADA até o momento no chunk.content
                    if hasattr(chunk, "content") and chunk.content is not None:
                        resposta_completa = chunk.content
                    elif hasattr(chunk, "messages") and len(chunk.messages) > 0:
                        # Fallback se o content vier vazio mas tiver mensagens
                        ultimo_msg = chunk.messages[-1]
                        if hasattr(ultimo_msg, "content"):
                            resposta_completa = ultimo_msg.content
                    elif isinstance(chunk, str):
                        # Se vier texto puro incremental
                        resposta_completa += chunk
                        
                    # Atualiza a tela imediatamente com o cursor piscante no final
                    placeholder.markdown(resposta_completa + "▌")
                
                # Tira o cursor piscante "▌" no final
                placeholder.markdown(resposta_completa)

                # PASSO C: Salva a resposta do robô na memória para não perder
                st.session_state.messages.append({"role": "assistant", "content": resposta_completa})
                
            except Exception as e:
                # Se algo der errado (ex: sem chave de API), mostra o erro
                erro_msg = f"⚠️ Ocorreu um erro: {str(e)}"
                st.error(erro_msg)
                st.session_state.messages.append({"role": "assistant", "content": erro_msg})

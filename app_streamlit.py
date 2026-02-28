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
                
                # ==========================================================
                # FUNÇÃO GERADORA DE DELTAS PARA O STREAMLIT
                # O modo Team do Agno envia o texto *acumulado* a cada tick 
                # e não as "novas palavras separadas". 
                # Para o Streamlit animar ("digitar ao vivo"), ele precisa de pedaços soltos.
                # ==========================================================
                def iterar_novas_palavras(stream):
                    texto_anterior = ""
                    for chunk in stream:
                        texto_atual = ""
                        
                        if hasattr(chunk, "content") and chunk.content is not None:
                            texto_atual = chunk.content
                        elif hasattr(chunk, "messages") and len(chunk.messages) > 0:
                            ultimo_msg = chunk.messages[-1]
                            if hasattr(ultimo_msg, "content") and ultimo_msg.content:
                                texto_atual = ultimo_msg.content
                        elif isinstance(chunk, str):
                            # Se por sorte vier como stream verdadeiro do python
                            texto_atual = texto_anterior + chunk
                            
                        # Só emite a "diferença" (as novas letrinhas que caíram)
                        if len(texto_atual) > len(texto_anterior):
                            delta = texto_atual[len(texto_anterior):]
                            texto_anterior = texto_atual
                            yield delta

                # O st.write_stream cuida da animação de digitação de geradores do python!
                resposta_completa = st.write_stream(iterar_novas_palavras(stream_response))

                # PASSO C: Salva a resposta do robô na memória para não perder
                st.session_state.messages.append({"role": "assistant", "content": resposta_completa})
                
            except Exception as e:
                # Se algo der errado (ex: sem chave de API), mostra o erro
                erro_msg = f"⚠️ Ocorreu um erro: {str(e)}"
                st.error(erro_msg)
                st.session_state.messages.append({"role": "assistant", "content": erro_msg})

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
# 2. BARRA LATERAL (SIDEBAR) & CONFIGURAÇÕES
# ============================================================
with st.sidebar:
    # URL de ícone mais profissional e futurista (Robô IA Estilizado)
    st.image("https://cdn-icons-png.flaticon.com/512/2814/2814666.png", width=60)
    st.markdown("### Agência Marketing IA")
    st.markdown("Agentes especializados focados em escalar os resultados digitais do seu negócio.")
    
    st.markdown("---")
    
    # Função para limpar o chat
    def limpar_chat():
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        
    st.button("🗑️ Limpar Conversa", on_click=limpar_chat, use_container_width=True)
    
    st.markdown("---")
    st.caption("Powered by [Agno](https://agno.com) & [Streamlit](https://streamlit.io)")


# ============================================================
# 3. INICIALIZAÇÃO DO ESTADO DA SESSÃO (Memória do App)
# ============================================================

# Se for a primeira vez que o usuário abre a página, cria um ID único para a sessão
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Cria uma lista vazia para guardar o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================
# 4. TELA INICIAL (QUANDO NÃO HÁ MENSAGENS)
# ============================================================
if len(st.session_state.messages) == 0:
    st.markdown("### 👋 Olá! Como posso ajudar hoje?")
    st.markdown("Escolha uma das sugestões abaixo ou digite o que precisa:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✍️ Escrever artigo blog", use_container_width=True):
            st.session_state.sugestao_clicada = "Escreva um artigo otimizado para SEO sobre: A importância do Marketing Digital para pequenos negócios."
            
        if st.button("📱 Criar post Instagram", use_container_width=True):
            st.session_state.sugestao_clicada = "Crie uma legenda de Instagram chamativa dando 3 dicas de como atrair mais clientes usando as redes sociais."
            
    with col2:
        if st.button("📧 Escrever Newsletter", use_container_width=True):
            st.session_state.sugestao_clicada = "Escreva um e-mail de vendas muito convincente oferecendo um serviço de Consultoria de SEO."
            
        if st.button("📅 Montar Calendário", use_container_width=True):
            st.session_state.sugestao_clicada = "Monte um calendário de conteúdo prático de 7 dias para o Instagram de uma pizzaria focada em delivery."


# ============================================================
# 3. DESENHAR O HISTÓRICO DE MENSAGENS NA TELA
# ============================================================
# Toda vez que a página recarregar, nós varremos a lista de mensagens salvas
# e desenhamos na tela novamente (balões de chat)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ============================================================
# 5. CAPTURAR A NOVA MENSAGEM DO USUÁRIO
# ============================================================
# Verifica se o usuário digitou na caixa OU clicou em um botão de sugestão
prompt = st.chat_input("Digite aqui o que você precisa...")

if "sugestao_clicada" in st.session_state:
    prompt = st.session_state.sugestao_clicada
    del st.session_state.sugestao_clicada # Limpa após usar

if prompt:
    
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
                        # Intercepta falhas silenciosas da API (JSON de Erro 429 injetado no stream pelo framework)
                        chunk_str = str(chunk)
                        if "429" in chunk_str and ("Quota exceeded" in chunk_str or "RESOURCE_EXHAUSTED" in chunk_str or "rate limit" in chunk_str.lower()):
                            raise Exception("API_QUOTA_EXCEEDED")
                            
                        texto_atual = ""
                        # Se for um obj de resposta do Agno (RunResponse)
                        if hasattr(chunk, "content") and chunk.content is not None:
                            # Ignora se for log técnico injetado pelo Agno em texto (ex: pesquisas web)
                            if isinstance(chunk.content, str) and "completed in" in chunk.content and "s." in chunk.content:
                                continue
                            texto_atual = chunk.content
                            
                        # Se vier em formato de array de mensagens
                        elif hasattr(chunk, "messages") and len(chunk.messages) > 0:
                            ultimo_msg = chunk.messages[-1]
                            # Só extrai se for o "assistant" falando, ignorando "tool"
                            if getattr(ultimo_msg, "role", "") == "assistant" and getattr(ultimo_msg, "content", None):
                                texto_atual = ultimo_msg.content
                                
                        # Se for pedaço de texto bruto (string iterada)
                        elif isinstance(chunk, str):
                            if ("completed in" in chunk and "s." in chunk) or chunk.startswith("Running:"):
                                continue
                            texto_atual = texto_anterior + chunk
                            
                        # Só emite a "diferença" se tivermos mais texto real do que tínhamos antes
                        if texto_atual and len(texto_atual) > len(texto_anterior):
                            delta = texto_atual[len(texto_anterior):]
                            texto_anterior = texto_atual
                            yield delta

                # O st.write_stream cuida da animação de digitação de geradores do python!
                resposta_completa = st.write_stream(iterar_novas_palavras(stream_response))

                # PASSO C: Salva a resposta do robô na memória para não perder
                st.session_state.messages.append({"role": "assistant", "content": resposta_completa})
                
            except Exception as e:
                erro_str = str(e)
                # Verifica se o erro é de Cota da API ou Limite de Taxa (Google/Groq/OpenAI, etc)
                if "429" in erro_str or "Quota exceeded" in erro_str or "RESOURCE_EXHAUSTED" in erro_str or "rate limit" in erro_str.lower():
                    erro_msg = (
                        "🚨 **Aviso: Limite da IA Atingido!**\n\n"
                        "A cota de uso da API da inteligência artificial acabou por hoje ou você enviou muitas mensagens muito rápido. "
                        "Por favor, aguarde alguns minutos e tente novamente, ou atualize sua Chave de API nas configurações do painel."
                    )
                else:
                    erro_msg = f"⚠️ Ocorreu um erro inesperado: {erro_str}"
                    
                st.error(erro_msg)
                st.session_state.messages.append({"role": "assistant", "content": erro_msg})

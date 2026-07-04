import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Hub do Corretor", page_icon="🏢", layout="centered")

st.title("💼 Portal Estratégico do Corretor")
st.subheader("Consultas de empreendimentos, mapeamento e scripts de vendas.")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except KeyError:
    st.error("Erro: Chave de API não encontrada nas configurações do servidor.")
    st.stop()

# Aqui você coloca as regras da sua operação
SYSTEM_INSTRUCTION = """
Você é o assistente virtual da nossa plataforma imobiliária.
Seu objetivo é ajudar corretores iniciantes e experientes a encontrar informações sobre empreendimentos em São Paulo, regras do programa Minha Casa Minha Vida (MCMV), opções de locação e dicas de negociação.
Forneça sempre respostas profissionais, scripts de qualificação para WhatsApp e foque na conversão do cliente.
"""

st.write("---")
query = st.text_input(
    "O que você precisa agora?", 
    placeholder="Ex: Script de WhatsApp para cliente MCMV ou detalhes de locação na Zona Sul..."
)

if st.button("Buscar Informação", type="primary"):
    if query:
        with st.spinner("Consultando base de dados..."):
            try:
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=SYSTEM_INSTRUCTION
                )
                response = model.generate_content(query)
                st.success("Resultado:")
                st.write(response.text)
            except Exception as e:
                st.error("Erro na busca. Tente novamente em alguns segundos.")
    else:
        st.warning("Digite uma dúvida para buscar.")

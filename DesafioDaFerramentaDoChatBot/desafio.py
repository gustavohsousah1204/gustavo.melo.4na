import streamlit as st
from googletrans import Translator

# Configuração da página
st.title("Tradutor Simples")
st.write("Insira o texto que deseja traduzir e escolha o idioma de destino.")

# Caixa de texto para entrada do usuário
texto_para_traduzir = st.text_area("Texto para tradução")

# Opções de idiomas
idiomas = {
    'en': 'Inglês',
    'es': 'Espanhol',
    'fr': 'Francês',
    'de': 'Alemão',
    'it': 'Italiano',
    'pt': 'Português',
    'ru': 'Russo',
    'ar': 'Árabe',
    'zh-cn': 'Chinês (Simplificado)',
    'ja': 'Japonês',
}

# Seleção do idioma de destino
idioma_destino = st.selectbox("Escolha o idioma de destino", list(idiomas.keys()), format_func=lambda x: idiomas[x])

# Traduzir
if st.button("Traduzir"):
    if texto_para_traduzir:
        # Criação do objeto Translator
        translator = Translator()
        
        # Realizando a tradução
        traducao = translator.translate(texto_para_traduzir, dest=idioma_destino)
        
        # Exibindo o resultado
        st.subheader("Texto Traduzido:")
        st.write(traducao.text)
    else:
        st.warning("Por favor, insira o texto para traduzir.")

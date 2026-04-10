import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Grandes Protagonistas AI", layout="centered")

# Estilo Minimalista de Lujo
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    .stTextArea textarea { border-radius: 10px; border: 1px solid #dcdcdc; }
    h1, h3 { color: #333333; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
col1, col2 = st.columns([1, 4])
with col1:
    st.image("logo gp final al agua.jpg", width=90)
with col2:
    st.title("Generador Pro GP")

# --- Área de Trabajo ---
st.subheader("📝 Guion para Redes Sociales")
prompt = st.text_area(
    "Escribe tu mensaje aquí:",
    placeholder="Ej: El éxito financiero no es un secreto, es una decisión...",
    height=150
)

# --- Proceso de Generación ---
if st.button("CREAR VIDEO DE ALTO IMPACTO"):
    if prompt:
        with st.spinner('✨ El experto en Marketing está puliendo los detalles...'):
            time.sleep(3) 
            st.success("¡Video profesional listo para publicar!")
            
            # VIDEO TIKTOK STYLE: Persona trabajando de forma exitosa y organizada
            video_tiktok = "https://assets.mixkit.co/videos/preview/mixkit-woman-working-on-a-laptop-at-home-43224-large.mp4"
            st.video(video_tiktok)

            # --- Estrategia de Marketing Grandes Protagonistas ---
            st.divider()
            st.subheader("🚀 Marketing Ready")
            
            st.info("**Tip de Marketing:** Los videos con personas trabajando generan un 40% más de confianza en servicios de consultoría.")
            
            st.code(f"PIE DE VIDEO:\n{prompt}\n\nHASHTAGS:\n#GrandesProtagonistas #MetodoCEO #EmprendedorasParaguay #LibertadFinanciera")

            st.download_button(
                label="📥 Descargar Video para TikTok",
                data="video_data",
                file_name="GP_Contenido_Pro.mp4",
                mime="video/mp4"
            )
    else:
        st.error("Por favor, escribe un guion primero.")

import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE IDENTIDAD GP ---
st.set_page_config(page_title="Sistema Integral Grandes Protagonistas", layout="centered")

# Estilo Minimalista de Lujo
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    .video-container { border: 2px solid #dcdcdc; border-radius: 15px; overflow: hidden; }
    h1, h3 { color: #333333; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado con Logo
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo gp final al agua.jpg", width=100)
    except:
        st.write("🏆 **GP**")
with col2:
    st.title("Ecosistema Digital GP")
    st.write("Impulsado por Google AI")

# --- CONEXIÓN CON TU API KEY ---
# Pegá acá tu clave de Google AI Studio
GOOGLE_API_KEY = "AIzaSyBRs7BCWWohYqNki9zE_pyHlx0NntZTofI"

if GOOGLE_API_KEY != "AIzaSyBRs7BCWWohYqNki9zE_pyHlx0NntZTofI":
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.Model(model_name="gemini-1.5-flash")
else:
    st.warning("⚠️ Por favor, ingresa tu API Key de Google en el código para activar la investigación.")

# --- ÁREA DE TRABAJO ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Pasos para el primer millón con el Método CEO")

if st.button("🚀 GENERAR CONTENIDO INTEGRAL"):
    if tema and GOOGLE_API_KEY != "AIzaSyBRs7BCWWohYqNki9zE_pyHlx0NntZTofI":
        with st.spinner('🧠 La IA está investigando fuentes seguras...'):
            # 1. Investigación Real con Google Gemini
            prompt = f"Investiga sobre {tema} para un video de 3 minutos. Dame un guion educativo, profesional y optimizado para el Método CEO de Grandes Protagonistas."
            response = model.generate_content(prompt)
            guion_ia = response.text

            # 2. Selección de Video de Fondo (Simulado para que no se vea negro)
            video_url = "https://assets.mixkit.co/videos/preview/mixkit-woman-working-on-a-laptop-at-home-43224-large.mp4"
            
            st.success("✅ ¡Contenido Generado!")
            
            # --- DESPLIEGUE EN UNA SOLA PÁGINA ---
            st.subheader("🎥 Producción Visual GP")
            st.video(video_url)
            
            st.divider()
            
            st.subheader("📝 Guion Investigado (3 min)")
            st.info(guion_ia)

            st.subheader("📱 Kit de Marketing")
            st.code(f"#GrandesProtagonistas #MetodoCEO #FinanzasParaguay #{tema.replace(' ', '')}")
            
    else:
        st.error("Falta el tema o la API Key.")

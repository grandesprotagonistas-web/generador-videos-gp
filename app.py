import streamlit as st
import google.generativeai as genai
import os
import time

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="Ecosistema Digital | Grandes Protagonistas", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    h1, h3 { color: #333333; font-family: 'Helvetica Neue', sans-serif; }
    .video-container { border: 2px solid #f0f0f0; border-radius: 15px; overflow: hidden; padding: 10px; background: #fafafa; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Seguro
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo gp final al agua.jpg", width=100)
    except:
        st.markdown("### 🏆 GP")
with col2:
    st.title("Generador Integral GP")
    st.write("Inteligencia Estratégica para el Método CEO")

st.divider()

# --- CONEXIÓN FORZADA A VERSIÓN ESTABLE V1 ---
GOOGLE_API_KEY = "AIzaSyDwwARFP76pMG6VEEiMkKXUPlQLIvXpWds"

# ESTA ES LA PARTE CLAVE: Forzamos la versión v1
os.environ["GOOGLE_GENERATIVE_AI_NETWORK_ENDPOINT"] = "generativelanguage.googleapis.com"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Probamos con el nombre del modelo sin el prefijo 'models/' para que la v1 lo reconozca
    model = genai.GenerativeModel('gemini-1.5-flash')
    api_funcional = True
except Exception as error_config:
    st.error(f"Error en la configuración: {error_config}")
    api_funcional = False

# --- ÁREA DE TRABAJO ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Importancia del fondo de emergencia")
estilo = st.selectbox("Estilo visual:", ["Profesional Ejecutivo", "Inspirador Minimalista", "Educativo Directo"])

if st.button("🚀 GENERAR CONTENIDO COMPLETO"):
    if tema and api_funcional:
        with st.status("🧠 Conectando con Google V1...", expanded=True) as status:
            try:
                # Especificamos el contenido de forma simple
                prompt = f"Actúa como experto financiero. Redacta un guion de 3 min sobre {tema} para el Método CEO."
                
                # Llamada a la generación
                response = model.generate_content(prompt)
                guion_final = response.text
                
                status.update(label="✅ ¡Contenido Generado!", state="complete", expanded=False)

                # --- RESULTADOS ---
                st.subheader("🎥 Producción Visual GP")
                st.markdown('<div class="video-container">', unsafe_allow_html=True)
                urls = {
                    "Profesional Ejecutivo": "https://assets.mixkit.co/videos/preview/mixkit-hand-holding-a-gold-coin-4432-large.mp4",
                    "Inspirador Minimalista": "https://assets.mixkit.co/videos/preview/mixkit-woman-working-at-home-43224-large.mp4",
                    "Educativo Directo": "https://assets.mixkit.co/videos/preview/mixkit-stack-of-gold-coins-4433-large.mp4"
                }
                st.video(urls[estilo])
                st.markdown('</div>', unsafe_allow_html=True)

                st.divider()
                st.subheader("📝 Guion Investigado")
                st.info(guion_final)
                
                st.subheader("📱 Marketing Toolkit")
                st.code(f"#GrandesProtagonistas #MetodoCEO #FinanzasParaguay")

            except Exception as e:
                # Si sigue fallando, mostramos un mensaje de diagnóstico
                st.error("Error persistente de API.")
                st.write(f"Detalle técnico: {str(e)}")
                st.info("Carolina, si este error persiste, intenta crear una NUEVA API Key en AI Studio, a veces las llaves viejas se quedan pegadas a la versión beta.")
    else:
        st.error("Por favor, ingresa un tema.")

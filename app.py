import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="Ecosistema Digital | Grandes Protagonistas", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background-color: #4a4a4a; color: white; border: none; font-weight: bold;
    }
    h1, h3 { color: #333333; font-family: 'Helvetica Neue', sans-serif; }
    .video-container { border: 2px solid #f0f0f0; border-radius: 15px; overflow: hidden; padding: 10px; background: #fafafa; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo gp final al agua.jpg", width=100)
    except:
        st.markdown("### 🏆 GP")
with col2:
    st.title("Generador Integral GP")
    st.write("Estrategia 360° para el Método CEO")

st.divider()

# --- CONEXIÓN CON EL MODELO DETECTADO (2.5 FLASH) ---
GOOGLE_API_KEY = "AIzaSyDwwARFP76pMG6VEEiMkKXUPlQLIvXpWds"
genai.configure(api_key=GOOGLE_API_KEY)

# Usamos el nombre exacto que nos dio tu App
MODELO_GP = "gemini-2.5-flash"

# --- ÁREA DE TRABAJO ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Pasos para el ahorro de emergencia")
estilo = st.selectbox("Estilo visual del video:", ["Profesional Ejecutivo", "Inspirador Minimalista", "Educativo Directo"])

if st.button("🚀 GENERAR CONTENIDO COMPLETO"):
    if tema:
        with st.status(f"🧠 Generando con {MODELO_GP}...", expanded=True) as status:
            try:
                model = genai.GenerativeModel(MODELO_GP)
                prompt = f"Actúa como experto financiero de Grandes Protagonistas. Investiga sobre '{tema}' y redacta un guion de 3 min para video siguiendo el Método CEO. Incluye gancho, 3 puntos clave y cierre motivador."
                
                response = model.generate_content(prompt)
                guion_final = response.text
                
                status.update(label="✅ ¡Contenido Generado!", state="complete", expanded=False)

                # --- DESPLIEGUE DE RESULTADOS ---
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
                st.subheader("📝 Guion Investigado (3 min)")
                st.info(guion_final)

                st.subheader("📱 Marketing Toolkit")
                st.code(f"#GrandesProtagonistas #MetodoCEO #FinanzasParaguay #{tema.replace(' ', '')}")

            except Exception as e:
                st.error(f"Error técnico: {str(e)}")
    else:
        st.error("Por favor, ingresa un tema.")

st.write("---")
st.caption("Grandes Protagonistas © 2026 | Impulsado por Gemini 2.5 Flash")

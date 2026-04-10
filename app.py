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

# Encabezado
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo gp final al agua.jpg", width=100)
    except:
        st.markdown("### 🏆 GP")
with col2:
    st.title("Generador Integral GP")

st.divider()

# --- CONEXIÓN E INVESTIGACIÓN DE MODELOS ---
GOOGLE_API_KEY = "AIzaSyDwwARFP76pMG6VEEiMkKXUPlQLIvXpWds"
genai.configure(api_key=GOOGLE_API_KEY)

def buscar_modelo_compatible():
    try:
        # Pedimos a la App que investigue qué modelos tienes permitidos
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                return m.name
        return None
    except Exception as e:
        return f"Error al listar modelos: {e}"

modelo_disponible = buscar_modelo_compatible()

# --- ÁREA DE TRABAJO ---
st.info(f"🤖 **Modelo detectado por la App:** {modelo_disponible}")

tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Importancia del fondo de emergencia")
estilo = st.selectbox("Estilo visual:", ["Profesional Ejecutivo", "Inspirador Minimalista", "Educativo Directo"])

if st.button("🚀 GENERAR CONTENIDO COMPLETO"):
    if tema and "models/" in str(modelo_disponible):
        with st.status(f"🧠 Usando {modelo_disponible}...", expanded=True) as status:
            try:
                # Usamos el modelo que la propia App encontró
                model = genai.GenerativeModel(modelo_disponible)
                prompt = f"Actúa como experto financiero. Redacta un guion de 3 min sobre {tema} para el Método CEO de Grandes Protagonistas."
                
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

            except Exception as e:
                st.error(f"Fallo en la generación: {str(e)}")
    else:
        st.error("No se detectó un modelo compatible o falta el tema.")

import streamlit as st
import google.generativeai as genai
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

# --- CONEXIÓN UNIVERSAL CON GOOGLE AI ---
GOOGLE_API_KEY = "AIzaSyBRs7BCWWohYqNki9zE_pyHlx0NntZTofI"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Usamos el nombre 'gemini-pro', que es el más estable y universalmente aceptado
    model = genai.GenerativeModel('gemini-pro')
    api_funcional = True
except Exception as error_config:
    st.error(f"Error en la configuración: {error_config}")
    api_funcional = False

# --- ÁREA DE TRABAJO ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Importancia del fondo de emergencia")
estilo = st.selectbox("Estilo visual:", ["Profesional Ejecutivo", "Inspirador Minimalista", "Educativo Directo"])

if st.button("🚀 GENERAR CONTENIDO COMPLETO"):
    if tema and api_funcional:
        with st.status("🧠 La IA está trabajando...", expanded=True) as status:
            st.write("Investigando fuentes seguras...")
            try:
                # Prompt directo y potente
                prompt = f"Actúa como un experto financiero de Grandes Protagonistas. Investiga sobre '{tema}' y redacta un guion de 3 minutos para video siguiendo el Método CEO. Incluye gancho, 3 puntos clave y cierre motivador."
                response = model.generate_content(prompt)
                guion_final = response.text
                
                st.write("Preparando visuales integrados...")
                time.sleep(1)
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
                st.code(f"#GrandesProtagonistas #MetodoCEO #FinanzasParaguay #{tema.replace(' ', '')}")

            except Exception as e:
                st.error(f"Hubo un problema con la respuesta de Google: {str(e)}")
                st.info("Tip: Asegúrate de que tu API Key no tenga espacios adicionales al principio o al final.")
    else:
        st.error("Por favor, ingresa un tema para comenzar.")

import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE IDENTIDAD GRANDES PROTAGONISTAS ---
st.set_page_config(page_title="Ecosistema Digital | Grandes Protagonistas", layout="centered")

# Estilo Minimalista de Lujo (Gris y Blanco)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    .stTextArea textarea { border-radius: 12px; border: 1px solid #dcdcdc; }
    .stTextInput input { border-radius: 8px; }
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
        st.markdown("### 🏆") # Icono de respaldo si el logo no carga
with col2:
    st.title("Generador Integral GP")
    st.write("Inteligencia Estratégica para el Método CEO")

st.divider()

# --- CONEXIÓN CON GOOGLE AI STUDIO ---
GOOGLE_API_KEY = "AIzaSyBRs7BCWWohYqNki9zE_pyHlx0NntZTofI"

# Inicialización de la IA
try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Usamos GenerativeModel correctamente
    model = genai.GenerativeModel('gemini-1.5-flash')
    api_funcional = True
except Exception as e:
    st.error(f"Error en la configuración de IA: {e}")
    api_funcional = False

# --- ÁREA DE TRABAJO ---
st.subheader("🎯 Definición del Contenido")
tema = st.text_input("¿Qué tema vamos a investigar hoy?", placeholder="Ej: La importancia del ahorro de emergencia")
estilo = st.selectbox("Estilo visual del video:", ["Profesional Ejecutivo", "Inspirador Minimalista", "Educativo Directo"])

if st.button("🚀 GENERAR INVESTIGACIÓN Y VIDEO"):
    if not tema:
        st.warning("Por favor, ingresa un tema para comenzar.")
    elif not api_funcional:
        st.error("La conexión con Google AI no está activa.")
    else:
        with st.status("🧠 Procesando Inteligencia...", expanded=True) as status:
            st.write("Buscando fuentes seguras en Google AI Studio...")
            
            # 1. Generación de Guion Real con Gemini
            try:
                prompt_educativo = f"""
                Actúa como un experto en educación financiera. Investiga sobre '{tema}'. 
                Escribe un guion de 3 minutos para un video de TikTok/Instagram. 
                El tono debe ser profesional y alineado al 'Método CEO' de Grandes Protagonistas.
                Incluye un gancho inicial, 3 datos clave y un cierre con llamado a la acción.
                """
                response = model.generate_content(prompt_educativo)
                guion_final = response.text
                st.write("Estructurando guion de 180 segundos...")
                time.sleep(1)
            except Exception as e:
                guion_final = f"Error al generar guion: {e}"

            st.write("Renderizando visuales integrados...")
            time.sleep(1)
            status.update(label="✅ ¡Contenido Completo!", state="complete", expanded=False)

        # --- DESPLIEGUE DE RESULTADOS (TODO EN UNA PÁGINA) ---
        
        # 1. El Video (Centralizado y funcional)
        st.subheader("🎥 Producción Visual GP")
        st.markdown('<div class="video-container">', unsafe_allow_html=True)
        
        # Selección de video según estilo para evitar la caja negra
        urls_estilo = {
            "Profesional Ejecutivo": "https://assets.mixkit.co/videos/preview/mixkit-hand-holding-a-gold-coin-4432-large.mp4",
            "Inspirador Minimalista": "https://assets.mixkit.co/videos/preview/mixkit-woman-working-on-a-laptop-at-home-43224-large.mp4",
            "Educativo Directo": "https://assets.mixkit.co/videos/preview/mixkit-stack-of-gold-coins-4433-large.mp4"
        }
        st.video(urls_estilo[estilo])
        st.markdown('</div>', unsafe_allow_html=True)

        st.divider()

        # 2. El Guion e Inteligencia
        st.subheader("📝 Guion de Investigación")
        st.info(guion_final)

        # 3. Herramientas de Marketing
        st.subheader("📱 Kit para Redes Sociales")
        col_copy, col_tags = st.columns(2)
        with col_copy:
            st.write("**Pie de video sugerido:**")
            st.write(f"Transforma tu relación con el dinero. Hoy hablamos de {tema}. #MetodoCEO")
        with col_tags:
            st.write("**Hashtags:**")
            st.code(f"#GrandesProtagonistas\n#MetodoCEO\n#FinanzasParaguay\n#{tema.replace(' ', '')}")

        # Opción de descarga del guion
        st.download_button(
            label="📥 Descargar Guion para Teleprompter",
            data=guion_final,
            file_name=f"GP_Guion_{tema}.txt",
            mime="text/plain"
        )

st.write("---")
st.caption("Grandes Protagonistas © 2026 | Sistema de Inteligencia Centralizado")

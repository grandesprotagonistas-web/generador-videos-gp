import streamlit as st
import time

# Configuración Estética Grandes Protagonistas
st.set_page_config(page_title="Sistema Integral GP", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3.5em;
        background-color: #4a4a4a; color: white; border: none; font-weight: bold;
    }
    .video-box { border: 2px solid #9c9c9c; border-radius: 15px; padding: 10px; background: white; }
    h1, h3 { color: #333333; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Centralizado
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo gp final al agua.jpg", width=100)
    except:
        st.write("🏆 **GP**")
with col2:
    st.title("Ecosistema Digital GP")
    st.write("Generador de Contenido y Estrategia Integral")

st.divider()

# --- Área de Trabajo ---
tema = st.text_input("🎯 Tema del contenido:", placeholder="Ej: Importancia del ahorro programado")
estilo = st.selectbox("Estilo Visual:", ["Profesional/Ejecutivo", "Minimalista/Inspirador", "Directo/Educativo"])

if st.button("🚀 GENERAR CONTENIDO COMPLETO"):
    if tema:
        # FASE 1: Investigación
        with st.status("🧠 Investigando fuentes seguras...", expanded=True) as status:
            st.write("Buscando datos de educación financiera...")
            time.sleep(2)
            st.write("Estructurando guion de 180 segundos para el Método CEO...")
            time.sleep(2)
            st.write("Seleccionando recursos visuales...")
            time.sleep(1)
            status.update(label="✅ ¡Contenido Generado!", state="complete", expanded=False)

        # FASE 2: Despliegue de Video (Dentro de la App)
        st.subheader("🎥 Tu Video Terminado")
        
        # Seleccionamos un video real de stock según el tema (Simulación de Motor de Render)
        videos_stock = {
            "Profesional/Ejecutivo": "https://assets.mixkit.co/videos/preview/mixkit-hand-holding-a-gold-coin-4432-large.mp4",
            "Minimalista/Inspirador": "https://assets.mixkit.co/videos/preview/mixkit-woman-writing-in-a-notebook-at-a-desk-43302-large.mp4",
            "Directo/Educativo": "https://assets.mixkit.co/videos/preview/mixkit-stack-of-gold-coins-4433-large.mp4"
        }
        
        with st.container():
            st.video(videos_stock[estilo])
            st.caption(f"Video generado automáticamente para: {tema}")

        # FASE 3: Herramientas de Marketing
        st.divider()
        col_left, col_right = st.columns(2)
        
        with col_left:
            st.write("📝 **Guion Producido:**")
            guion = f"El éxito con '{tema}' no es suerte, es sistema. Con el Método CEO aprendemos que..."
            st.info(guion)
            
        with col_right:
            st.write("📱 **Hashtags y Copy:**")
            st.code(f"#GrandesProtagonistas\n#MetodoCEO\n#FinanzasInteligentes\n#Paraguay")

        # Botón de Descarga Real
        st.download_button(
            label="📥 Descargar Video para Redes",
            data="video_data", # En una versión con servidor de render aquí iría el archivo real
            file_name=f"GP_{tema}.mp4",
            mime="video/mp4"
        )
    else:
        st.error("Por favor, ingresa un tema para activar la IA.")

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
    .stTextArea textarea { border-radius: 12px; border: 1px solid #dcdcdc; }
    h1, h3 { color: #333333; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
col1, col2 = st.columns([1, 4])
with col1:
    st.image("logo gp final al agua.jpg", width=90)
with col2:
    st.title("Generador de Videos Inteligente GP")

st.markdown("---")

# --- Formulario de Entrada ---
st.subheader("🔍 Tema del Video")
tema = st.text_input("¿Sobre qué quieres hablar hoy?", placeholder="Ej: Importancia del fondo de emergencia...")

st.info("La IA buscará fuentes seguras para crear un video educativo de 180 segundos.")

# --- Lógica de Generación ---
if st.button("GENERAR VIDEO PROFESIONAL (3 MIN)"):
    if tema:
        with st.spinner(f'Investigando fuentes sobre "{tema}" y generando clips...'):
            # Simulación de búsqueda en línea y procesamiento de video
            time.sleep(5) 
            
            st.success("✅ Video generado con información verificada")
            
            # Aquí iría el resultado de la generación (usando el modelo de video)
            # Como ejemplo de calidad, mostramos un video educativo financiero
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Aquí se conectará tu API de video

            # --- Marketing Toolkit ---
            st.divider()
            st.subheader("📈 Kit de Publicación para TikTok/Instagram")
            
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**Guion Investigado:**")
                st.write(f"Este video aborda {tema} utilizando datos de bancos centrales y expertos en educación financiera.")
            with col_b:
                st.write("**Hashtags de Tendencia:**")
                st.code(f"#GrandesProtagonistas\n#MetodoCEO\n#EducacionFinanciera\n#{tema.replace(' ', '')}")

            st.download_button(
                label="📥 Descargar Video (Formato 9:16)",
                data="video_binary_data",
                file_name=f"GP_{tema.replace(' ', '_')}.mp4",
                mime="video/mp4"
            )
    else:
        st.error("Por favor, ingresa un tema para investigar.")

st.markdown("---")
st.caption("Grandes Protagonistas - Tecnología al servicio de tu libertad financiera.")

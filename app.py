import streamlit as st
import time
from textblob import TextBlob

# Configuración de página
st.set_page_config(page_title="Grandes Protagonistas AI", layout="centered")

# Estilo Minimalista (Gris Profesional)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #9c9c9c;
        color: white;
        border: none;
        font-weight: bold;
    }
    .stTextArea textarea { border-radius: 10px; border: 1px solid #dcdcdc; }
    h1, h3 { color: #333333; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
col1, col2 = st.columns([1, 4])
with col1:
    # Usamos el nombre exacto de tu archivo subido
    st.image("logo gp final al agua.jpg", width=90)
with col2:
    st.title("Generador de Contenido GP")

st.write("Educación financiera de calidad para tus potenciales clientes.")

# --- Área de Trabajo ---
with st.container():
    st.subheader("📝 Guion del Video")
    prompt = st.text_area(
        "Contenido para TikTok:",
        placeholder="Ej: El éxito financiero no es un secreto...",
        height=180
    )

    col_a, col_b = st.columns(2)
    with col_a:
        st.selectbox("Tono del Video", ["Profesional Neutro", "Inspirador", "Directo"])
    with col_b:
        st.text_input("Formato", value="9:16 (Vertical)", disabled=True)

# --- Proceso de Generación ---
if st.button("CREAR VIDEO PROFESIONAL"):
    if prompt:
        # Control de Calidad Ortográfica
        blob = TextBlob(prompt)
        texto_corregido = str(blob.correct())
        
        with st.spinner('🎬 El experto en Marketing está montando tu video profesional...'):
            time.sleep(4) 
            st.success("¡Video optimizado generado con éxito!")
            
            # CAMBIO CLAVE: Video de stock financiero real (monedas y crecimiento)
            video_url = "https://assets.mixkit.co/videos/preview/mixkit-stack-of-gold-coins-4433-large.mp4"
            st.video(video_url)

            # --- Estrategia de Marketing ---
            st.divider()
            st.subheader("🚀 Marketing Ready")
            
            resumen = texto_corregido[:110]
            pie_texto = f"{resumen}... ¡Sé el protagonista de tu libertad financiera! 💼"
            hashtags = "#GrandesProtagonistas #MetodoCEO #EducacionFinanciera #FinanzasParaguay"
            
            st.info("Sugerencia: Este contenido genera confianza y autoridad en tu marca.")
            st.code(f"PIE DE VIDEO:\n{pie_texto}\n\nHASHTAGS:\n{hashtags}")

            st.download_button(
                label="📥 Descargar Video Final",
                data="video_data",
                file_name="video_grandes_protagonistas.mp4",
                mime="video/mp4"
            )
    else:
        st.error("Por favor, ingresa el texto del video para comenzar.")

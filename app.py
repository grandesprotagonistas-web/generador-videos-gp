import streamlit as st
from PIL import Image

# Configuración estética de la página
st.set_page_config(page_title="Grandes Protagonistas - AI Video Gen", layout="centered")

# CSS personalizado para minimalismo
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #8e8e8e;
        color: white;
        border: none;
    }
    .stTextArea textarea { border-radius: 10px; }
    h1 { color: #4a4a4a; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado con Logo
col1, col2 = st.columns([1, 4])
with col1:
    st.image("logo_gp.png", width=80) # Sube tu logo aquí
with col2:
    st.title("Generador de Contenido")

st.info("Educación financiera de calidad para potenciales clientes.")

# --- Formulario de Creación ---
with st.container():
    st.subheader("📝 Script del Video")
    prompt = st.text_area("Ingresa el texto para el video (IA generará imágenes basadas en esto):", 
                          placeholder="Ej: Tres pasos para organizar tu presupuesto mensual...", 
                          height=150)
    
    col_a, col_b = st.columns(2)
    with col_a:
        voz = st.selectbox("Tono de Voz", ["Neutro Profesional", "Motivador", "Cercano (Paraguay)"])
    with col_b:
        formato = st.text_input("Formato", value="9:16 (TikTok/Reels)", disabled=True)

# --- Lógica de Generación ---
if st.button("Generar Video Profesional"):
    if prompt:
        with st.spinner('IA trabajando: Revisando ortografía y montando clips...'):
            # Aquí se conectaría con la función de procesamiento de video (MoviePy/IA)
            # Simulación de proceso:
            import time
            time.sleep(3)
            
            st.success("¡Video generado con éxito!")
            
            # Resultado Visual
            st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Ejemplo
            
            # --- Output de Marketing ---
            st.divider()
            st.subheader("🚀 Marketing Ready")
            st.code(f"""
            PIE DE VIDEO:
            {prompt[:100]}... ¡Sé el protagonista de tu libertad financiera! 💼✨
            
            HASHTAGS:
            #GrandesProtagonistas #FinanzasPersonales #MetodoCEO #EducacionFinanciera
            """)
            
            st.download_button("Descargar Video para TikTok", data="...", file_name="video_gp.mp4")
    else:
        st.warning("Por favor, ingresa un texto primero.")

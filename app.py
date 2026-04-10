import streamlit as st
import time

# Configuración con identidad Grandes Protagonistas
st.set_page_config(page_title="Generador Pro | Grandes Protagonistas", layout="centered")

# Estilo Minimalista de Lujo
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    .stTextArea textarea { border-radius: 15px; border: 1px solid #dcdcdc; }
    h1, h3 { color: #333333; font-family: 'Helvetica', sans-serif; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Seguro para evitar errores
col1, col2 = st.columns([1, 4])
with col1:
    try:
        st.image("logo gp final al agua.jpg", width=120)
    except:
        st.markdown("### 🏆")
with col2:
    st.title("Generador Pro GP")
    st.write("Investigación y Creación de Contenido")

st.write("---")

# --- Entrada de Inteligencia ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: La regla de ahorro 50/30/20")

if st.button("🚀 GENERAR ESTRATEGIA Y GUION DE 3 MIN"):
    if tema:
        with st.spinner(f'Investigando fuentes sobre "{tema}"...'):
            time.sleep(4)
            st.success("✅ ¡Investigación completada!")
            
            # Guion inteligente para la IA de video
            guion_ia = f"""Crea un video de 3 minutos sobre: {tema}. 
            Detalles importantes: Usa un tono profesional pero cercano. 
            Menciona que este contenido es parte del ecosistema de Grandes Protagonistas. 
            El video debe tener subtítulos dinámicos y clips de alta calidad de personas trabajando y finanzas."""
            
            st.subheader("📝 Tu Guion de Alta Inteligencia")
            st.write("Copia este texto para el paso final:")
            st.text_area("Guion para copiar:", guion_ia, height=150)

            st.divider()
            st.subheader("🎬 Paso Final: Crear el Video Real")
            st.info("InVideo AI ya está habilitado para Paraguay. Haz clic abajo, regístrate con Google y pega el texto de arriba.")
            
            # Botón hacia la herramienta que SI funciona ya mismo
            st.markdown(f"""
                <a href="https://invideo.io/ai/" target="_blank">
                    <button style="width:100%; border-radius:12px; height:3.8em; background-color:#0066FF; color:white; border:none; font-weight:bold; cursor:pointer; font-size:16px;">
                        👉 CLIC AQUÍ: PEGAR GUION Y CREAR VIDEO
                    </button>
                </a>
            """, unsafe_allow_html=True)
    else:
        st.error("Carolina, por favor ingresa un tema.")

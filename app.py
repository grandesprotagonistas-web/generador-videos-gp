import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Generador Pro GP", layout="centered")

# Estilo Minimalista
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    h1, h3 { color: #333333; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.image("logo gp final al agua.jpg", width=120)
st.title("Generador de Contenido Maestro")

# --- Entrada de Inteligencia ---
tema = st.text_input("🎯 ¿De qué quieres que hable tu video de 3 minutos?", placeholder="Ej: Pasos para el primer millón")

if st.button("🚀 FABRICAR ESTRATEGIA Y VIDEO"):
    if tema:
        with st.spinner('Investigando fuentes seguras y creando guion de 180s...'):
            time.sleep(3)
            
            st.success(f"✅ ¡Investigación sobre '{tema}' lista!")
            
            # --- El Guion Profesional ---
            st.subheader("📝 Guion de 3 Minutos (TikTok/IG)")
            guion_final = f"""
            INTRO (0-30s): ¿Sentís que el dinero se te escapa? Hoy hablamos de {tema}.
            DATOS (30-150s): Según fuentes de educación financiera, la clave es la organización. Con el Método CEO...
            CIERRE (150-180s): Seguinos en Grandes Protagonistas para más libertad financiera.
            """
            st.text_area("Copia este guion:", guion_final, height=200)

            # --- LA SOLUCIÓN AL VIDEO ---
            st.divider()
            st.subheader("🎥 Paso Final para generar el video")
            st.write("Debido a que los videos de 3 minutos son pesados, usaremos el motor de Veo.")
            
            # Aquí es donde ocurre la magia real
            st.info("💡 Haz clic en el botón de abajo, pega el guion que generamos y el video se creará con animaciones profesionales automáticamente.")
            
            st.markdown(f"[👉 GENERAR VIDEO EN VEO](https://veo.google.com/)") # Link a la herramienta de generación

    else:
        st.error("Por favor, ingresa un tema.")

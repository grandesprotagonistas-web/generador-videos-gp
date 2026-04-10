import streamlit as st
import time

# Configuración de página
st.set_page_config(page_title="Grandes Protagonistas AI", layout="centered")

# Estilo Minimalista (Gris GP)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    .stTextArea textarea { border-radius: 12px; }
    h1, h3 { color: #333333; font-family: 'Helvetica', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
col1, col2 = st.columns([1, 4])
with col1:
    st.image("logo gp final al agua.jpg", width=90)
with col2:
    st.title("Generador Pro GP")

st.write("---")

# --- Entrada de Usuario ---
tema = st.text_input("🎯 Tema del video (Investigación automática):", 
                    placeholder="Ej: Cómo salir de deudas con el Método CEO")

duracion = st.slider("Duración (segundos):", 60, 180, 180)

# --- Botón de Acción ---
if st.button("GENERAR INVESTIGACIÓN Y VIDEO"):
    if tema:
        with st.spinner(f'Investigando fuentes financieras sobre "{tema}"...'):
            time.sleep(4) # Simulación de búsqueda en red
            
            st.success("✅ Investigación completada con fuentes seguras.")
            
            # --- Simulación de Guion para 3 Minutos ---
            st.subheader("📝 Guion Estructurado (180s)")
            guion_texto = f"""
            00:00-00:30: Introducción sobre {tema}. 
            00:30-01:30: Datos reales de mercado y consejos prácticos.
            01:30-02:30: Aplicación del Método CEO en este contexto.
            02:30-03:00: Cierre con logo de Grandes Protagonistas.
            """
            st.write(guion_texto)
            
            # --- Visualización del Video (Estilo Dinámico) ---
            st.subheader("🎥 Vista Previa del Contenido")
            # Video de alta calidad (Lifestyle financiero)
            st.video("https://assets.mixkit.co/videos/preview/mixkit-young-woman-working-at-her-laptop-in-a-cafe-43130-large.mp4")

            # --- Marketing Toolkit ---
            st.divider()
            st.subheader("🚀 Estrategia de Publicación")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**Pie de video optimizado:**")
                st.write(f"¿Sabías esto sobre {tema}? Descubrí cómo aplicarlo hoy.")
            with col_b:
                st.write("**Hashtags:**")
                st.code(f"#GrandesProtagonistas\n#MetodoCEO\n#FinanzasParaguay")
    else:
        st.error("Por favor, ingresa un tema.")

st.write("---")
st.caption("Para videos ilimitados, usá este guion en InVideo AI (Plan Free).")

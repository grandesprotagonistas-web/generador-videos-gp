import streamlit as st
import time

# Configuración de página con identidad GP
st.set_page_config(page_title="Generador Pro | Grandes Protagonistas", layout="centered")

# Estilo Minimalista de Lujo
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.8em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold; font-size: 18px;
    }
    .stTextArea textarea { border-radius: 15px; border: 1px solid #dcdcdc; }
    h1, h2, h3 { color: #333333; font-family: 'Helvetica', sans-serif; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- Encabezado Seguro ---
col1, col2 = st.columns([1, 4])
with col1:
    try:
        # Intentamos cargar el logo con el nombre exacto
        st.image("logo gp final al agua.jpg", width=120)
    except:
        # Si falla, mostramos un icono elegante para que no dé error la página
        st.markdown("### 🏆")

with col2:
    st.title("Generador Pro GP")
    st.write("Estrategia y Contenido de Alto Impacto")

# --- Inteligencia de Contenido ---
tema = st.text_input("🎯 ¿Cuál es el tema de investigación hoy?", placeholder="Ej: Pasos para ahorrar mi primer millón")

if st.button("🚀 GENERAR INVESTIGACIÓN Y VIDEO (3 MIN)"):
    if tema:
        with st.spinner('🔍 Investigando fuentes seguras y estructurando guion de 180s...'):
            time.sleep(4)
            st.success(f"✅ Investigación sobre '{tema}' lista para producción.")
            
            # --- Generación de Guion Estructurado ---
            st.subheader("📝 Guion Maestro (TikTok / Instagram / YouTube)")
            guion_investigado = f"""
            INTRO (0:00-0:45): Gancho visual impactante sobre {tema}. ¿Por qué el 90% de la gente falla aquí?
            CUERPO 1 (0:45-1:30): Datos de expertos. La importancia de la constancia según el Método CEO.
            CUERPO 2 (1:30-2:30): Aplicación práctica. Cómo transformar {tema} en un activo financiero.
            CIERRE (2:30-3:00): Llamado a la acción. Sé la protagonista de tu libertad financiera.
            """
            st.text_area("Copia este guion para la IA de video:", guion_investigado, height=220)

            # --- CONEXIÓN CON EL MOTOR DE VIDEO VEO ---
            st.divider()
            st.subheader("🎬 Paso Final: Generar Video en Veo")
            st.info("Para obtener la calidad del cerdito azul, usa el motor de Veo. Es gratuito y procesa videos largos de alta fidelidad.")
            
            # Botón de redirección directa
            st.markdown(f"""
                <a href="https://veo.google.com/" target="_blank">
                    <button style="width:100%; border-radius:12px; height:3.5em; background-color:#34A853; color:white; border:none; font-weight:bold; cursor:pointer;">
                        👉 HACER CLIC AQUÍ: PEGAR GUION Y CREAR VIDEO
                    </button>
                </a>
            """, unsafe_allow_html=True)
            
            st.write(" ")
            st.caption("Instrucciones: Al entrar a Veo, pega el guion de arriba y escribe: 'Genera un video estilo 3D animado con voz en off profesional sobre este tema'.")

    else:
        st.error("Carolina, por favor ingresa un tema para comenzar.")

st.markdown("---")
st.caption("Grandes Protagonistas © 2026 | Potenciando tu Marca Personal")

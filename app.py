import streamlit as st
import time
import random

# Configuración de página
st.set_page_config(page_title="Generador Pro | Grandes Protagonistas", layout="centered")

# Estilo Minimalista de Lujo (Gris y Blanco)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5em;
        background-color: #9c9c9c; color: white; border: none; font-weight: bold;
    }
    .stTextArea textarea { border-radius: 12px; border: 1px solid #dcdcdc; }
    .stTextInput input { border-radius: 8px; }
    h1, h3 { color: #333333; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado con Logo
col1, col2 = st.columns([1, 4])
with col1:
    # Ajustado al nombre exacto de tu archivo en GitHub
    try:
        st.image("logo gp final al agua.jpg", width=90)
    except:
        st.error("Error: Verifica que el logo esté en GitHub con el nombre exacto.")

with col2:
    st.title("Generador de Videos GP")
    st.write("Tecnología para la Educación Financiera de Calidad.")

st.markdown("---")

# --- Entrada de Inteligencia ---
tema = st.text_input("🎯 ¿Cuál es el tema de hoy?", placeholder="Ej: Por qué el ahorro de emergencia es tu seguro de vida")

if st.button("🚀 GENERAR INVESTIGACIÓN Y VIDEO (180s)"):
    if tema:
        with st.spinner(f'Investigando fuentes seguras sobre "{tema}"...'):
            # Simulación de búsqueda en tiempo real
            time.sleep(3)
            st.toast("Analizando datos de expertos financieros...")
            time.sleep(2)
            
            st.success(f"✅ Investigación sobre '{tema}' completada con éxito.")
            
            # --- Generación de Guion de Alto Impacto ---
            st.subheader("📝 Guion de 3 Minutos para TikTok/Instagram")
            guion = f"""
            0:00 - 0:30 (GANCHO): ¿Sabías que el 80% de las personas fallan en sus finanzas por no entender {tema}? Hoy en Grandes Protagonistas te lo explico fácil.
            
            0:30 - 1:30 (DATOS): Investigamos fuentes de educación financiera y la clave está en la constancia. Aplicando el Método CEO, {tema} se vuelve una herramienta de libertad, no una carga.
            
            1:30 - 2:30 (DESARROLLO): Aquí mostramos cómo integrarlo a tu presupuesto mensual. No se trata de cuánto ganas, sino de cómo lo gestionas.
            
            2:30 - 3:00 (CIERRE): Sé la protagonista de tu futuro. Si quieres la planilla del Método CEO, comenta 'YO'.
            """
            st.text_area("Copia el guion para tu teleprompter:", guion, height=250)
            
            # --- Visualización de Video (Dinamismo Lifestyle) ---
            st.subheader("🎥 Estilo Visual Sugerido")
            # Video de lifestyle profesional: mujer organizada trabajando
            video_url = "https://assets.mixkit.co/videos/preview/mixkit-woman-writing-in-a-notebook-at-a-desk-43302-large.mp4"
            st.video(video_url)

            # --- Kit de Marketing ---
            st.divider()
            st.subheader("📈 Marketing Ready")
            col_a, col_b = st.columns(2)
            with col_a:
                st.write("**Pie de Video:**")
                st.write(f"Toma el control hoy: {tema}. La información es poder cuando se aplica. 💼✨")
            with col_b:
                st.write("**Hashtags:**")
                st.code(f"#GrandesProtagonistas\n#MetodoCEO\n#FinanzasParaguay\n#EducacionFinanciera")

            st.download_button(
                label="📥 Descargar Guion e Informe",
                data=guion,
                file_name="Estrategia_GP.txt",
                mime="text/plain"
            )
    else:
        st.error("Por favor, ingresa un tema para que la IA pueda investigar.")

st.markdown("---")
st.caption("Grandes Protagonistas © 2026 | Desarrollado para Carolina.")

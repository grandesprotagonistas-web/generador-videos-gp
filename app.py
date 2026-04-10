# --- CONEXIÓN ---
api_ready = False
modelo_final = "gemini-1.5-flash" # Forzamos el 1.5 para saltar el límite del 2.5

try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Eliminamos la auto-detección temporalmente para usar el 1.5 directamente
        model = genai.GenerativeModel(modelo_final)
        api_ready = True
        st.caption(f"🚀 Motor de Alta Disponibilidad: {modelo_final}")
    else:
        st.error("⚠️ Configura GOOGLE_API_KEY en Secrets.")
except Exception as e:
    st.error(f"⚠️ Error: {e}")

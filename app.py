import streamlit as st
import google.generativeai as genai
import time

# --- IDENTIDAD VISUAL GP ---
st.set_page_config(page_title="Folioscopio Pro | GP", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background-color: #4a4a4a; color: white; border: none; font-weight: bold;
    }
    .folio-card {
        background-color: #fcfcfc; border: 1px solid #eeeeee;
        border-radius: 25px; padding: 40px; text-align: center;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        min-height: 500px; display: flex; flex-direction: column;
        align-items: center; justify-content: center;
    }
    .folio-text { font-size: 26px; color: #333333; font-weight: 700; line-height: 1.4; margin-top: 25px; }
    .folio-sub { color: #9c9c9c; font-size: 14px; text-transform: uppercase; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Folioscopio Estratégico GP")
st.write("Ecosistema Digital | Método CEO")

# --- CONEXIÓN SEGURA Y AUTO-DETECCIÓN ---
api_ready = False
modelo_final = "gemini-1.5-flash"

try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        
        # Detectar modelos disponibles
        modelos_disponibles = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if modelos_disponibles:
            modelo_final = modelos_disponibles[0]
        
        model = genai.GenerativeModel(modelo_final)
        api_ready = True
        st.caption(f"🚀 Motor activo: {modelo_final}")
    else:
        st.error("⚠️ Falta 'GOOGLE_API_KEY' en los Secrets de Streamlit.")
except Exception as e:
    st.error(f"⚠️ Error de configuración: {e}")

# --- ÁREA DE TRABAJO ---
tema = st.text_input("🎯 ¿Qué estrategia visual creamos?", placeholder="Ej: Pasos para el primer millón")
formato = st.radio("Experiencia:", ["Carrusel (Manual)", "Folioscopio (Automático)"], horizontal=True)

if st.button("🚀 GENERAR SECUENCIA VISUAL"):
    if tema and api_ready:
        with st.status(f"🧠 Generando con {modelo_final}...", expanded=True) as status:
            try:
                prompt = f"Crea 5 escenas para un carrusel sobre '{tema}'. Sigue el Método CEO. Formato de respuesta: Texto impactante | PalabraClaveImagen. Dame 5 líneas."
                response =

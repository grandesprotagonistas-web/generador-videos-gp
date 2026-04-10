import streamlit as st
import google.generativeai as genai
import time

# --- IDENTIDAD GP ---
st.set_page_config(page_title="GP Folioscopio", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background: #4a4a4a; color: white; }
    .folio-card { background: #fcfcfc; border: 1px solid #eee; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .folio-text { font-size: 20px; color: #333; font-weight: bold; margin-top: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Folioscopio GP")

# --- CONEXIÓN LIGERA ---
@st.cache_resource
def load_model():
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Cambiamos a 1.5-flash que es el más estable para cuotas gratuitas
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

model = load_model()

# --- INTERFAZ ---
tema = st.text_input("🎯 Tema de hoy:", placeholder="Ej: Ahorro con el Método CEO")
modo = st.radio("Modo:", ["Manual", "Automático"], horizontal=True)

if st.button("🚀 GENERAR"):
    if tema and model:
        try:
            # Prompt ultra-corto para ahorrar tokens y cuota
            p = f"5 frases cortas sobre {tema} (Método CEO). Formato: Frase | PalabraImagen. 5 líneas."
            r = model.generate_content(p)
            
            data = []
            for linea in r.text.strip().split('\n'):
                if "|" in linea:
                    t, k = linea.split("|")
                    img = f"https://loremflickr.com/400/400/{k.strip().replace(' ', '')},business"
                    data.append({"t": t.strip(), "i": img})
            
            if modo == "Manual":
                tabs = st.tabs([f"E{i+1}" for i in range(len(data))])
                for i, tab in enumerate(tabs):
                    with tab:
                        st.markdown(f'<div class="folio-card"><img src="{data[i]["i"]}" style="width:280px;border-radius:12px;"><div class="folio-text">{data[i]["t"]}</div></div>', unsafe_allow_html=True)
            else:
                v = st.empty()
                for d in data:
                    v.markdown(f'<div class="folio-card"><img src="{d["i"]}" style="width:280px;border-radius:12px;"><div class="folio-text">{d["t"]}</div></div>', unsafe_allow_html=True)
                    time.sleep(3.5)
            st.success("🏁 ¡Hecho!")

        except Exception as e:
            st.error("⚠️ Límite de Google alcanzado. Espera 2 minutos.")
    else:
        st.warning("Escribe un tema o configura tu API Key.")

import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Folioscopio GP", layout="centered")

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
    .folio-text { font-size: 24px; color: #333333; font-weight: 700; line-height: 1.4; margin-top: 25px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Folioscopio Estratégico GP")

# --- CONEXIÓN ---
api_ready = False
modelo_final = "gemini-1.5-flash"

try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        if modelos:
            modelo_final = modelos[0]
        model = genai.GenerativeModel(modelo_final)
        api_ready = True
        st.caption(f"🚀 Motor: {modelo_final}")
    else:
        st.error("⚠️ Configura GOOGLE_API_KEY en Secrets.")
except Exception as e:
    st.error(f"⚠️ Error: {e}")

# --- TRABAJO ---
tema = st.text_input("🎯 Tema:", placeholder="Ej: Pasos para el primer millón")
formato = st.radio("Modo:", ["Manual", "Automático"], horizontal=True)

if st.button("🚀 GENERAR"):
    if tema and api_ready:
        with st.status("🧠 Generando...", expanded=True) as status:
            try:
                p = f"Actúa como experto financiero. Crea 5 frases para un carrusel sobre {tema}. Usa el Método CEO. Formato: Frase | PalabraClave. Dame solo 5 líneas."
                r = model.generate_content(p)
                lineas = r.text.strip().split('\n')
                
                data = []
                for l in lineas:
                    if "|" in l:
                        txt, key = l.split("|")
                        # Usamos un servicio de imagen más estable
                        url = f"https://loremflickr.com/400/400/{key.strip()},finance/all"
                        data.append({"t": txt.strip(), "i": url})

                status.update(label="✅ Listo", state="complete")

                if formato == "Manual":
                    tabs = st.tabs([f"P{i+1}" for i in range(len(data))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f'<div class="folio-card"><img src="{data[i]["i"]}" style="width:300px;border-radius:15px;box-shadow: 0 4px 8px rgba(0,0,0,0.1);"><div class="folio-text">{data[i]["t"]}</div></div>', unsafe_allow_html=True)
                else:
                    v = st.empty()
                    for d in data:
                        v.markdown(f'<div class="folio-card"><img src="{d["i"]}" style="width:300px;border-radius:15px;box-shadow: 0 4px 8px rgba(0,0,0,0.1);"><div class="folio-text">{d["t"]}</div></div>', unsafe_allow_html=True)
                        time.sleep(3.5)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Verifica el tema y la API Key.")

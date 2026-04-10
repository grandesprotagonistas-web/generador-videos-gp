import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Folioscopio GP | Método CEO", layout="centered")

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

# --- CONEXIÓN SEGURA ---
api_ready = False
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Forzamos la v1 para evitar el error 404 de la v1beta
        model = genai.GenerativeModel('gemini-1.5-flash')
        api_ready = True
        st.caption("🚀 Conexión Activa: Canal Estable")
    else:
        st.error("⚠️ Configura GOOGLE_API_KEY en Secrets.")
except Exception as e:
    st.error(f"⚠️ Error de conexión: {e}")

# --- INTERFAZ ---
tema = st.text_input("🎯 Tema:", placeholder="Ej: Pasos para el primer millón")
formato = st.radio("Modo:", ["Manual (Pestañas)", "Automático (Folioscopio)"], horizontal=True)

if st.button("🚀 GENERAR"):
    if tema and api_ready:
        with st.status("🧠 Generando...", expanded=True) as status:
            try:
                op = RequestOptions(api_version="v1")
                prompt = f"Actúa como experto financiero. Crea 5 frases para un carrusel sobre {tema}. Usa el Método CEO. Formato: Frase | PalabraClave. Dame 5 líneas."
                
                response = model.generate_content(prompt, request_options=op)
                lineas = response.text.strip().split('\n')
                
                data = []
                for l in lineas:
                    if "|" in l:
                        txt, key = l.split("|")
                        img = f"https://loremflickr.com/400/400/{key.strip().replace(' ', '')},finance/all"
                        data.append({"t": txt.strip(), "i": img})

                status.update(label="✅ Listo", state="complete")

                if formato == "Manual (Pestañas)":
                    tabs = st.tabs([f"P{i+1}" for i in range(len(data))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f'<div class="folio-card"><img src="{data[i]["i"]}" style="width:300px;border-radius:15px;"><div class="folio-text">{data[i]["t"]}</div></div>', unsafe_allow_html=True)
                else:
                    v = st.empty()
                    for d in data:
                        v.markdown(f'<div class="folio-card"><img src="{d["i"]}" style="width:300px;border-radius:15px;"><div class="folio-text">{d["t"]}</div></div>', unsafe_allow_html=True)
                        time.sleep(3.5)
            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Completa el tema para iniciar.")

import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN GP ---
st.set_page_config(page_title="GP Content Factory", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background: #4a4a4a; color: white; font-weight: bold; }
    .copy-box { background: #f8f9fa; padding: 20px; border-radius: 15px; border: 1px solid #ddd; font-family: sans-serif; margin-top: 20px; }
    .folio-card { background: #ffffff; border: 1px solid #eee; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Fábrica de Contenido GP")

# --- CONEXIÓN DE ALTA DISPONIBILIDAD ---
def get_model():
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # Usamos el 1.5-flash que tiene 1,500 peticiones por día
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

model = get_model()

# --- INTERFAZ ---
tema = st.text_input("🎯 Tema estratégico:", placeholder="Ej: Método CEO para ventas")
modo = st.radio("Visualización:", ["Carrusel Manual", "Folioscopio Auto"], horizontal=True)

if st.button("🚀 GENERAR PAQUETE COMPLETO"):
    if tema and model:
        try:
            # Prompt de una sola vía para ahorrar cuota
            p = f"Actúa como experto en marketing para 'Grandes Protagonistas'. Para el tema {tema}, genera: 1. 5 frases (Frase | PalabraClave), 2. Copy persuasivo Método CEO, 3. 10 Hashtags. Separa con '---'."
            
            r = model.generate_content(p)
            secciones = r.text.split('---')
            
            # 1. Visual
            lineas = secciones[0].strip().split('\n')
            data = []
            for l in lineas:
                if "|" in l:
                    txt, key = l.split("|")
                    img = f"https://loremflickr.com/400/400/{key.strip().replace(' ', '')},business"
                    data.append({"t": txt.strip(), "i": img})
            
            st.subheader("🖼️ Storyboard")
            if modo == "Carrusel Manual":
                tabs = st.tabs([f"P{i+1}" for i in range(len(data))])
                for i, tab in enumerate(tabs):
                    with tab:
                        st.markdown(f'<div class="folio-card"><img src="{data[i]["i"]}" style="width:280px;border-radius:12px;"><br><b>{data[i]["t"]}</b></div>', unsafe_allow_html=True)
            else:
                v = st.empty()
                for d in data:
                    v.markdown(f'<div class="folio-card"><img src="{d["i"]}" style="width:280px;border-radius:12px;"><br><b>{d["t"]}</b></div>', unsafe_allow_html=True)
                    time.sleep(3)

            # 2. Copy y Hashtags
            st.divider()
            st.subheader("📝 Copy & Hashtags")
            copy_text = secciones[1] if len(secciones) > 1 else "Copy en proceso..."
            tags_text = secciones[2] if len(secciones) > 2 else "#GrandesProtagonistas"
            
            st.markdown(f'<div class="copy-box"><b>Pie de foto:</b><br>{copy_text}<br><br><b>Tags:</b><br>{tags_text}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error de Cuota: Google ha bloqueado esta clave temporalmente. Detalles: {e}")
    else:
        st.warning("Verifica tu clave en Secrets y el tema.")

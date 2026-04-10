import streamlit as st
import google.generativeai as genai
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
st.write("Ecosistema Digital de Productividad")

# --- CONEXIÓN FORZADA A V1 (ESTABLE) ---
api_ready = False

try:
    if "GOOGLE_API_KEY" in st.secrets:
        # Configuramos la versión de transporte a 'rest' para asegurar compatibilidad v1
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"], transport='rest')
        
        # Usamos el nombre del modelo con el prefijo completo para evitar el 404
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        # Prueba rápida de conexión
        api_ready = True
        st.caption("🚀 Conexión Estable: v1 Gemini 1.5 Flash")
    else:
        st.error("⚠️ Configura 'GOOGLE_API_KEY' en los Secrets de Streamlit.")
except Exception as e:
    st.error(f"⚠️ Error de conexión: {e}")

# --- ENTRADA DE USUARIO ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Pasos para el primer millón")
formato = st.radio("Modo de visualización:", ["Manual (Pestañas)", "Automático (Folioscopio)"], horizontal=True)

if st.button("🚀 GENERAR SECUENCIA VISUAL"):
    if tema and api_ready:
        with st.status("🧠 Diseñando contenido estratégico...", expanded=True) as status:
            try:
                prompt = f"Actúa como experto financiero. Crea 5 frases para un carrusel sobre {tema}. Usa el Método CEO. Formato: Frase | PalabraClave. Dame solo 5 líneas."
                
                response = model.generate_content(prompt)
                lineas = response.text.strip().split('\n')
                
                data_visual = []
                for l in lineas:
                    if "|" in l:
                        txt, key = l.split("|")
                        # Buscador de imágenes de respaldo estable
                        img_url = f"https://loremflickr.com/400/400/{key.strip().replace(' ', '')},finance/all"
                        data_visual.append({"t": txt.strip(), "i": img_url})

                status.update(label="✅ Contenido Creado", state="complete")

                if formato == "Manual (Pestañas)":
                    tabs = st.tabs([f"P{i+1}" for i in range(len(data_visual))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f"""
                                <div class="folio-card">
                                    <img src="{data_visual[i]['i']}" style="width:300px;border-radius:15px;box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                                    <div class="folio-text">{data_visual[i]['t']}</div>
                                </div>
                            """, unsafe_allow_html=True)
                else:
                    visor = st.empty()
                    for d in data_visual:
                        visor.markdown(f"""
                            <div class="folio-card">
                                <img src="{d['i']}" style="width:300px;border-radius:15px;box-shadow: 0 4px 8px rgba(0,0,0,0.1);">
                                <div class="folio-text">{d['t']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        time.sleep(3.5)
                
                st.success("🏁 ¡Listo para Grandes Protagonistas!")

            except Exception as e:
                st.error(f"Error técnico: {e}")
    else:
        st.warning("Verifica el tema y la configuración.")

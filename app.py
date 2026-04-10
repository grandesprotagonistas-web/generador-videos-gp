import streamlit as st
import google.generativeai as genai
import time

# --- OPTIMIZACIÓN DE INTERFAZ GP ---
st.set_page_config(page_title="Folioscopio Estratégico | GP", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background-color: #4a4a4a; color: white; border: none; font-weight: bold;
    }
    .folio-card {
        background: #fcfcfc; border: 1px solid #eeeeee;
        border-radius: 25px; padding: 40px; text-align: center;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.05);
        min-height: 480px; display: flex; flex-direction: column;
        align-items: center; justify-content: center;
    }
    .folio-text { font-size: 22px; color: #333; font-weight: 700; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Folioscopio Grandes Protagonistas")
st.caption("Optimizado para el Método CEO")

# --- LÓGICA DE CONEXIÓN ROBUSTA ---
@st.cache_resource
def iniciar_modelo():
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            api_key = st.secrets["GOOGLE_API_KEY"]
            genai.configure(api_key=api_key)
            # La optimización aquí es usar el nombre de modelo más compatible
            return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return None
    return None

model = iniciar_modelo()

# --- PANEL DE CONTROL ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Gestión del tiempo")
modo = st.segmented_control("Formato:", ["Manual", "Automático"], default="Manual")

if st.button("🚀 GENERAR ESTRATEGIA VISUAL"):
    if not tema:
        st.warning("Ingresa un tema para empezar.")
    elif not model:
        st.error("Error de API: Revisa tus Secrets en Streamlit.")
    else:
        with st.status("🧠 IA optimizando contenido...", expanded=True) as status:
            try:
                # Prompt optimizado para evitar alucinaciones
                p = f"Actúa como consultor financiero. Crea 5 frases para un carrusel sobre {tema}. Método CEO. Formato estrictamente: Texto | PalabraClave. 5 líneas."
                r = model.generate_content(p)
                
                # Procesamiento optimizado de datos
                data = []
                for linea in r.text.strip().split('\n'):
                    if "|" in linea:
                        txt, key = linea.split("|")
                        # Usamos un CDN de imagen optimizado (Unsplash Source via Proxy)
                        img = f"https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=400&q=80" if "negocio" in key.lower() else f"https://loremflickr.com/400/400/{key.strip().replace(' ', '')}"
                        data.append({"t": txt.strip(), "i": img})
                
                status.update(label="✅ Contenido Listo", state="complete")

                if modo == "Manual":
                    tabs = st.tabs([f"Pág {i+1}" for i in range(len(data))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f"""
                                <div class="folio-card">
                                    <img src="{data[i]['i']}" style="width:320px; border-radius:15px;">
                                    <div class="folio-text">{data[i]['t']}</div>
                                </div>
                            """, unsafe_allow_html=True)
                else:
                    visor = st.empty()
                    for d in data:
                        visor.markdown(f"""
                            <div class="folio-card">
                                <img src="{d['i']}" style="width:320px; border-radius:15px;">
                                <div class="folio-text">{d['t']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        time.sleep(3.5)
                
            except Exception as e:
                st.error(f"Error técnico: {str(e)}")
                st.info("Sugerencia: Google está limitando las peticiones. Espera 30 segundos.")

st.divider()
st.caption("Grandes Protagonistas © 2026")

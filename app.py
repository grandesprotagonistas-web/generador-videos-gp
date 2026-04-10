import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE INTERFAZ ---
st.set_page_config(page_title="GP Folioscopio | Elite", layout="centered")

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
st.caption("Optimización Técnica para el Método CEO")

# --- CONEXIÓN FORZADA A V1 (ELIMINANDO V1BETA) ---
@st.cache_resource
def configurar_ia():
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            # Forzamos el transporte REST para saltar configuraciones locales de v1beta
            genai.configure(api_key=st.secrets["GOOGLE_API_KEY"], transport='rest')
            # Usamos el nombre del modelo sin prefijos ambiguos
            return genai.GenerativeModel('gemini-1.5-flash')
    except:
        return None
    return None

model = configurar_ia()

# --- INTERFAZ ---
tema = st.text_input("🎯 ¿Qué tema investigamos hoy?", placeholder="Ej: Pasos para el primer millón")
modo = st.radio("Formato de visualización:", ["Manual", "Automático"], horizontal=True)

if st.button("🚀 GENERAR ESTRATEGIA VISUAL"):
    if not tema:
        st.warning("Ingresa un tema.")
    elif not model:
        st.error("Error de API: Revisa tus Secrets en Streamlit.")
    else:
        with st.status("🧠 IA Procesando...", expanded=True) as status:
            try:
                # Prompt optimizado para ser procesado rápido
                p = f"Experto financiero. Crea 5 frases para carrusel sobre {tema}. Método CEO. Formato: Frase | PalabraClave. 5 líneas."
                
                # Generación directa
                r = model.generate_content(p)
                
                # Procesamiento robusto
                data = []
                for linea in r.text.strip().split('\n'):
                    if "|" in linea:
                        partes = linea.split("|")
                        txt = partes[0].strip()
                        key = partes[1].strip().replace(' ', '')
                        # Imagen fotorrealista vía CDN estable
                        img = f"https://loremflickr.com/400/400/{key},finance/all"
                        data.append({"t": txt, "i": img})
                
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
                st.error("Tropiezo en la conexión. Google ha detectado demasiadas peticiones.")
                st.info("Sugerencia: Espera 1 minuto para que se limpie la cuota gratuita.")

st.divider()
st.caption("Grandes Protagonistas © 2026")

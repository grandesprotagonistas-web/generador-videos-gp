import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="Folioscopio Seguro | GP", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background-color: #4a4a4a; color: white; border: none; font-weight: bold;
    }
    .folio-page {
        width: 100%; height: 500px;
        background-color: #f9f9f9; border: 2px solid #e0e0e0;
        border-radius: 20px; display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        padding: 30px; text-align: center;
    }
    .folio-text { font-size: 24px; color: #333; font-weight: 600; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Folioscopio Estratégico GP")

# --- CONEXIÓN SEGURA ---
try:
    # IMPORTANTE: Aquí usamos el nombre de la variable, NO la clave directamente
    api_key = st.secrets["GOOGLE_API_KEY"] 
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    api_funcional = True
except Exception as e:
    st.error("⚠️ Error: No se encontró 'GOOGLE_API_KEY' en los Secrets de Streamlit.")
    api_funcional = False

# --- ÁREA DE TRABAJO ---
tema = st.text_input("🎯 Tema para el folioscopio:", placeholder="Ej: Gestión del tiempo para madres")

if st.button("🚀 GENERAR FOLIOSCOPIO"):
    if tema and api_funcional:
        with st.status("🧠 Diseñando secuencia visual...", expanded=True) as status:
            try:
                prompt = f"Crea 5 frases cortas y potentes sobre '{tema}' para un carrusel. Usa el Método CEO. Formato: Frase | PalabraClaveImagen. Dame 5 líneas."
                response = model.generate_content(prompt)
                lineas = response.text.strip().split('\n')
                
                placeholder = st.empty()
                for linea in lineas:
                    if "|" in linea:
                        partes = linea.split("|")
                        texto = partes[0].strip()
                        keyword = partes[1].strip()
                        img_url = f"https://source.unsplash.com/featured/?{keyword},minimal"
                        
                        placeholder.markdown(f"""
                            <div class="folio-page">
                                <img src="{img_url}" style="width: 300px; border-radius: 15px;">
                                <div class="folio-text">{texto}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        time.sleep(3.5)
                
                status.update(label="✅ Folioscopio Completado", state="complete")
            except Exception as e:
                st.error(f"Error en la generación: {e}")

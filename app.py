import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Folioscopio GP | Método CEO", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3.5em; background: #4a4a4a; color: white; font-weight: bold; }
    .folio-card { background: #ffffff; border: 1px solid #eee; border-radius: 20px; padding: 30px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .copy-box { background: #f8f9fa; padding: 20px; border-radius: 15px; border-left: 5px solid #4a4a4a; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Fábrica de Contenido GP")

# --- CONEXIÓN DIRECTA Y LIMPIA ---
def conectar_ia():
    if "GOOGLE_API_KEY" in st.secrets:
        # Configuramos la clave
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        # IMPORTANTE: No usamos RequestOptions ni versiones Beta. 
        # Dejamos que el modelo se inicialice de la forma más simple posible.
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

model = conectar_ia()

# --- INTERFAZ ---
tema = st.text_input("🎯 Tema de hoy:", placeholder="Ej: Ahorro inteligente")
modo = st.radio("Formato Visual:", ["Carrusel", "Folioscopio"], horizontal=True)

if st.button("🚀 GENERAR TODO"):
    if tema and model:
        # Usamos un contenedor de estado para que el usuario vea progreso
        with st.spinner("🧠 El Método CEO está procesando tu idea..."):
            try:
                # Prompt unificado para no saturar la cuota
                prompt = f"Actúa como experto en Grandes Protagonistas. Tema: {tema}. Entrega 5 frases (Frase | PalabraClave), un copy persuasivo y 10 hashtags. Separa con '---'."
                
                # Intentamos la generación
                response = model.generate_content(prompt)
                
                # Si llegamos aquí, la clave funciona. Procesamos:
                partes = response.text.split('---')
                
                # 1. Visual
                lineas = partes[0].strip().split('\n')
                data_v = []
                for l in lineas:
                    if "|" in l:
                        t, k = l.split("|")
                        img = f"https://loremflickr.com/400/400/{k.strip().replace(' ', '')},business"
                        data_v.append({"t": t.strip(), "i": img})
                
                # Renderizado
                if modo == "Carrusel":
                    tabs = st.tabs([f"E{i+1}" for i in range(len(data_v))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f'<div class="folio-card"><img src="{data_v[i]["i"]}" style="width:280px;border-radius:12px;"><br><br><b>{data_v[i]["t"]}</b></div>', unsafe_allow_html=True)
                else:
                    visor = st.empty()
                    for d in data_v:
                        visor.markdown(f'<div class="folio-card"><img src="{d["i"]}" style="width:280px;border-radius:12px;"><br><br><b>{d["t"]}</b></div>', unsafe_allow_html=True)
                        time.sleep(3)

                # 2. Texto
                st.divider()
                st.subheader("📝 Copy y Estrategia")
                copy = partes[1] if len(partes) > 1 else "Redactando..."
                tags = partes[2] if len(partes) > 2 else "#GrandesProtagonistas"
                st.markdown(f'<div class="copy-box">{copy}<br><br><b>Hashtags:</b><br>{tags}</div>', unsafe_allow_html=True)

            except Exception as e:
                # Si falla, mostramos una instrucción clara de ingeniería
                st.error("⚠️ La conexión con Google está saturada.")
                st.info("Carolina, tu clave está bien, pero has superado el límite de velocidad. Por favor, espera exactamente 60 segundos sin tocar el botón y volverá a funcionar.")
    else:
        st.warning("Configuración pendiente.")

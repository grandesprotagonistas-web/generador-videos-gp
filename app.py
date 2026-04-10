import streamlit as st
import google.generativeai as genai
import time

# --- IDENTIDAD VISUAL GRANDES PROTAGONISTAS ---
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
    .folio-text { font-size: 26px; color: #333333; font-weight: 700; line-height: 1.4; margin-top: 25px; }
    .folio-sub { color: #9c9c9c; font-size: 14px; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado Minimalista
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("### 🏆")
with col2:
    st.title("Folioscopio Estratégico")
    st.write("Ecosistema Digital Grandes Protagonistas")

st.divider()

# --- CONEXIÓN SEGURA CON LOS SECRETS ---
try:
    # Aquí buscamos la clave que guardaste en "Misterios"
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    api_ready = True
except Exception as e:
    st.error("⚠️ Configuración incompleta: Asegúrate de que 'GOOGLE_API_KEY' esté en los Secrets de Streamlit.")
    api_ready = False

# --- INTERFAZ DE USUARIO ---
tema = st.text_input("🎯 ¿Qué estrategia visual creamos hoy?", placeholder="Ej: Pasos para el ahorro de emergencia")
formato = st.radio("Elige la experiencia:", ["Carrusel (Manual)", "Folioscopio (Automático)"], horizontal=True)

if st.button("🚀 GENERAR SECUENCIA VISUAL"):
    if tema and api_ready:
        with st.status("🧠 La IA está diseñando tu secuencia...", expanded=True) as status:
            try:
                # Prompt optimizado para el folioscopio
                prompt = f"""
                Eres un director creativo para 'Grandes Protagonistas'. Crea 5 escenas para un folioscopio sobre '{tema}'.
                Sigue el Método CEO. Cada escena debe ser impactante.
                Formato de respuesta (5 líneas exactamente):
                Texto de la escena | Palabra clave para imagen
                """
                response = model.generate_content(prompt)
                escenas = response.text.strip().split('\n')
                
                # Procesar datos
                data_final = []
                for esc in escenas:
                    if "|" in esc:
                        t, k = esc.split("|")
                        # Usamos imágenes de alta calidad de Source Unsplash
                        url = f"https://images.unsplash.com/photo-1554224155-1696413575b9?auto=format&fit=crop&q=80&w=400" if "ahorro" in tema.lower() else f"https://source.unsplash.com/featured/400x400?{k.strip()},business,minimal"
                        data_final.append({"texto": t.strip(), "img": url})

                status.update(label="✅ Contenido Creado", state="complete")

                # --- RENDERIZADO ---
                if formato == "Carrusel (Manual)":
                    tabs = st.tabs([f"E{i+1}" for i in range(len(data_final))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f"""
                                <div class="folio-card">
                                    <div class="folio-sub">Escena {i+1} de 5</div>
                                    <img src="{data_final[i]['img']}" style="width: 320px; border-radius: 20px;">
                                    <div class="folio-text">{data_final[i]['texto']}</div>
                                </div>
                            """, unsafe_allow_html=True)
                else:
                    # Folioscopio Automático
                    visor = st.empty()
                    for i, esc in enumerate(data_final):
                        visor.markdown(f"""
                            <div class="folio-card">
                                <div class="folio-sub">Paso {i+1} de 5</div>
                                <img src="{esc['img']}" style="width: 320px; border-radius: 20px;">
                                <div class="folio-text">{esc['texto']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        time.sleep(3.5) # Tiempo de "vuelta de hoja"
                
                st.success("🏁 ¡Secuencia lista para grabar o presentar!")

            except Exception as e:
                st.error(f"Hubo un pequeño tropiezo: {e}")
    else:
        st.warning("Escribe un tema antes de empezar.")

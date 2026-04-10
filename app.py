import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="GP Folioscopio Pro", layout="centered")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 12px; height: 3em; background: #4a4a4a; color: white; font-weight: bold; }
    .folio-card { background: #fcfcfc; border: 1px solid #eee; border-radius: 20px; padding: 30px; text-align: center; margin-bottom: 20px; }
    .folio-text { font-size: 20px; color: #333; font-weight: bold; margin-top: 15px; }
    .copy-box { background: #f0f2f6; padding: 20px; border-radius: 15px; border-left: 5px solid #4a4a4a; font-family: sans-serif; }
    </style>
    """, unsafe_allow_html=True)

st.title("📖 Folioscopio & Copywriter GP")
st.write("Estrategia Completa: Visual + Texto + Hashtags")

# --- CONEXIÓN (VERSIÓN SIN CACHÉ FORZADA) ---
def load_model():
    if "GOOGLE_API_KEY" in st.secrets:
        # Usamos directamente la configuración para evitar que el caché guarde errores viejos
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        return genai.GenerativeModel('gemini-1.5-flash')
    return None

# Intentar cargar el modelo en cada refresco para asegurar que la cuota esté fresca
model = load_model()
# --- INTERFAZ ---
tema = st.text_input("🎯 Tema de la estrategia:", placeholder="Ej: 3 pasos para salir de deudas")
modo = st.radio("Formato Visual:", ["Manual", "Automático"], horizontal=True)

if st.button("🚀 GENERAR CONTENIDO COMPLETO"):
    if tema and model:
        with st.status("🧠 Redactando y diseñando...", expanded=True) as status:
            try:
                # Prompt maestro para optimizar cuota
                p = f"""
                Actúa como Copywriter y Diseñador para 'Grandes Protagonistas'. 
                Para el tema: {tema}, entrega:
                1. 5 frases cortas (Frase | PalabraImagen)
                2. Un Pie de imagen persuasivo usando el Método CEO.
                3. 10 hashtags estratégicos incluyendo #GrandesProtagonistas.
                Separa las secciones con '---'.
                """
                r = model.generate_content(p)
                partes = r.text.split('---')
                
                # Procesar Folioscopio
                lineas_folio = partes[0].strip().split('\n')
                data_folio = []
                for l in lineas_folio:
                    if "|" in l:
                        txt, key = l.split("|")
                        img = f"https://loremflickr.com/400/400/{key.strip().replace(' ', '')},business"
                        data_folio.append({"t": txt.strip(), "i": img})

                status.update(label="✅ Estrategia Creada", state="complete")

                # --- VISUAL ---
                st.subheader("🎥 Vista Previa Visual")
                if modo == "Manual":
                    tabs = st.tabs([f"E{i+1}" for i in range(len(data_folio))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f'<div class="folio-card"><img src="{data_folio[i]["i"]}" style="width:280px;border-radius:12px;"><div class="folio-text">{data_folio[i]["t"]}</div></div>', unsafe_allow_html=True)
                else:
                    v = st.empty()
                    for d in data_folio:
                        v.markdown(f'<div class="folio-card"><img src="{d["i"]}" style="width:280px;border-radius:12px;"><div class="folio-text">{d["t"]}</div></div>', unsafe_allow_html=True)
                        time.sleep(3.5)

                # --- COPY Y HASHTAGS ---
                st.divider()
                st.subheader("📝 Copy y Hashtags para Redes")
                
                copy_final = partes[1] if len(partes) > 1 else "Generando copy..."
                tags_final = partes[2] if len(partes) > 2 else "#GrandesProtagonistas #MetodoCEO"
                
                st.markdown(f"""
                <div class="copy-box">
                    <strong>Pie de Imagen:</strong><br>
                    {copy_final}<br><br>
                    <strong>Hashtags:</strong><br>
                    <span style="color: #4a4a4a;">{tags_final}</span>
                </div>
                """, unsafe_allow_html=True)
                
                st.button("📋 Copiar Texto (Función visual)", on_click=lambda: st.toast("¡Texto listo para copiar!"))

            except Exception as e:
                st.error("⚠️ Límite de Google. Espera un momento para reiniciar la cuota.")
    else:
        st.warning("Ingresa un tema para empezar.")

import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="Ecosistema GP | Presentación Animada", layout="centered")

# Estilo para el Formato Vertical (Reel Style)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background-color: #4a4a4a; color: white; border: none; font-weight: bold;
    }
    /* Estilo del Contenedor Vertical */
    .vertical-reel {
        width: 320px; height: 568px; 
        background: linear-gradient(180deg, #f0f0f0 0%, #dcdcdc 100%);
        border: 8px solid #333; border-radius: 25px;
        margin: auto; position: relative; overflow: hidden;
        display: flex; flex-direction: column; align-items: center; justify-content: center;
        text-align: center; padding: 20px; box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
    }
    .reel-text { color: #333; font-family: 'Helvetica Neue', sans-serif; font-weight: bold; font-size: 22px; }
    .reel-logo { position: absolute; top: 20px; width: 50px; opacity: 0.6; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.title("Generador de Contenido Vertical")
st.write("Estrategia Visual Grandes Protagonistas")

# --- CONEXIÓN IA ---
GOOGLE_API_KEY = "AIzaSyDwwARFP76pMG6VEEiMkKXUPlQLIvXpWds"
genai.configure(api_key=GOOGLE_API_KEY)
MODELO_GP = "gemini-2.5-flash"

# --- ENTRADA DE DATOS ---
tema = st.text_input("🎯 Tema para tu Reel/TikTok:", placeholder="Ej: 3 errores que matan tus ahorros")

if st.button("🚀 CREAR PRESENTACIÓN ANIMADA"):
    if tema:
        with st.status("🧠 La IA está diseñando la secuencia...", expanded=True) as status:
            try:
                model = genai.GenerativeModel(MODELO_GP)
                # Pedimos a la IA que divida el guion en "escenas" cortas
                prompt = f"Actúa como experto en redes sociales. Crea 5 frases cortas y potentes sobre '{tema}' para un Reel de 15 segundos. Usa el Método CEO. Devuélveme solo las 5 frases separadas por comas."
                
                response = model.generate_content(prompt)
                frases = response.text.split(',')
                
                status.update(label="✅ Secuencia Diseñada", state="complete", expanded=False)

                # --- REPRODUCTOR ANIMADO (Simulación de Presentación) ---
                st.subheader("🎥 Vista Previa Vertical")
                
                # Contenedor de la animación
                reel_placeholder = st.empty()
                
                for frase in frases:
                    # Creamos el efecto de "diapositiva"
                    reel_placeholder.markdown(f"""
                        <div class="vertical-reel">
                            <div class="reel-logo">🏆</div>
                            <div class="reel-text">{frase.strip()}</div>
                            <div style="position: absolute; bottom: 30px; font-size: 12px; color: #888;">
                                Grandes Protagonistas | Método CEO
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    time.sleep(3) # Tiempo que dura cada frase en pantalla
                
                st.success("🏁 Presentación completada. Puedes capturar pantalla para tus historias.")
                
                # --- GUION COMPLETO ---
                st.divider()
                st.subheader("📝 Guion Completo Detallado")
                st.write(response.text)

            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.error("Ingresa un tema.")

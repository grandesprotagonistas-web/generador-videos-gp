import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE IDENTIDAD ---
st.set_page_config(page_title="Folioscopio Digital | Grandes Protagonistas", layout="centered")

# Estilo para el Carrusel/Folioscopio
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%; border-radius: 12px; height: 3.5em;
        background-color: #4a4a4a; color: white; border: none; font-weight: bold;
    }
    .folio-page {
        width: 100%; height: 450px;
        background-color: #f9f9f9;
        border: 2px solid #e0e0e0;
        border-radius: 20px;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        padding: 30px; text-align: center;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    }
    .folio-text { font-size: 24px; color: #333; font-weight: 600; margin-top: 20px; }
    .folio-header { color: #9c9c9c; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.title("📖 Folioscopio Estratégico GP")
st.write("Contenido Visual en Secuencia | Método CEO")

# --- CONEXIÓN IA ---
GOOGLE_API_KEY = "AIzaSyDwwARFP76pMG6VEEiMkKXUPlQLIvXpWds"
genai.configure(api_key=GOOGLE_API_KEY)
MODELO_GP = "gemini-2.5-flash"

# --- ÁREA DE TRABAJO ---
tema = st.text_input("🎯 ¿Sobre qué creamos el folioscopio hoy?", placeholder="Ej: Los 5 pilares del ahorro")
modo = st.radio("Selecciona el formato visual:", ["Carrusel Manual", "Folioscopio Automático"])

if st.button("🚀 GENERAR SECUENCIA VISUAL"):
    if tema:
        with st.status("🧠 La IA está ilustrando tu estrategia...", expanded=True) as status:
            try:
                model = genai.GenerativeModel(MODELO_GP)
                # Pedimos a la IA que cree 5 "páginas" de folioscopio
                prompt = f"""
                Actúa como diseñador instruccional. Para el tema '{tema}', crea 5 páginas para un folioscopio.
                Cada página debe tener:
                1. Una frase corta y potente (Máximo 10 palabras).
                2. Una palabra clave para buscar una imagen descriptiva.
                Formato: Frase | PalabraClave
                Dame solo las 5 líneas.
                """
                response = model.generate_content(prompt)
                lineas = response.text.strip().split('\n')
                
                status.update(label="✅ Folioscopio Listo", state="complete", expanded=False)

                # --- RENDERIZADO DEL FOLIOSCOPIO ---
                st.subheader("🖼️ Resultado Visual")
                
                paginas_contenido = []
                for linea in lineas:
                    if "|" in linea:
                        partes = linea.split("|")
                        texto = partes[0].strip()
                        keyword = partes[1].strip()
                        # Usamos Unsplash para obtener imágenes reales basadas en la IA
                        img_url = f"https://source.unsplash.com/featured/?{keyword},finance,minimal"
                        paginas_contenido.append({"texto": texto, "img": img_url})

                if modo == "Carrusel Manual":
                    # Carrusel usando pestañas de Streamlit
                    tabs = st.tabs([f"Pág {i+1}" for i in range(len(paginas_contenido))])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.markdown(f"""
                                <div class="folio-page">
                                    <div class="folio-header">Escena {i+1}</div>
                                    <img src="{paginas_contenido[i]['img']}" style="width: 250px; border-radius: 15px; margin-bottom: 20px;">
                                    <div class="folio-text">{paginas_contenido[i]['texto']}</div>
                                </div>
                            """, unsafe_allow_html=True)
                
                else:
                    # Folioscopio Automático (Efecto de paso de página)
                    placeholder = st.empty()
                    for i, pag in enumerate(paginas_contenido):
                        placeholder.markdown(f"""
                            <div class="folio-page">
                                <div class="folio-header">Paso {i+1} de 5</div>
                                <img src="{pag['img']}" style="width: 280px; border-radius: 15px; margin-bottom: 20px;">
                                <div class="folio-text">{pag['texto']}</div>
                            </div>
                        """, unsafe_allow_html=True)
                        time.sleep(3) # Velocidad del folioscopio
                
                st.success("🏁 Secuencia terminada. ¡Ideal para grabar como Reel!")

            except Exception as e:
                st.error(f"Error de cuota o conexión: Espera 60 segundos. Detalle: {e}")
    else:
        st.error("Por favor, ingresa un tema.")

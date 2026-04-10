# --- CONEXIÓN CON GOOGLE AI STUDIO ---
GOOGLE_API_KEY = "AIzaSyBRs7BCWWohYqNki9zE_pyHlx0NntZTofI"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Intentamos con el nombre del modelo estándar
    # Si da error 404, el sistema probará automáticamente la versión estable
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        # Prueba rápida para validar el modelo
        model.generate_content("Hola") 
    except:
        model = genai.GenerativeModel('gemini-pro') # Modelo de respaldo garantizado
        
    api_funcional = True
except Exception as e:
    st.error(f"Error en la configuración de IA: {e}")
    api_funcional = False

import streamlit as st
import google.generativeai as genai
from google.generativeai.types import RequestOptions # Importación clave para forzar la v1
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

# --- CONEXIÓN FORZADA A V1 ---
api_ready = False

try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
        
        # Configuramos las

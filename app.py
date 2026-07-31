"""
Punto de entrada de la app. Orquesta los módulos, sin contener lógica de detalle.
Ejecutar con: streamlit run app.py
"""

import streamlit as st

from config import APP_TITLE, APP_ICON, PATH_IMAGEN_MASCOTA
from image_utils import cargar_imagen_local_base64, imagen_a_data_url
from styles import inject_css
from ui.state import init_session_state
from ui.header import render_header
from ui.sidebar import render_sidebar
from ui.chat import render_historial, handle_chat_input

# --- Configuración de página (debe ser la primera llamada de Streamlit) ---
st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout="centered")

# --- Estado, estilos y recursos ---
init_session_state()
inject_css()

patu_b64 = cargar_imagen_local_base64(PATH_IMAGEN_MASCOTA)
patu_avatar_url = imagen_a_data_url(None, b64=patu_b64, mime="image/png") if patu_b64 else "🦆"

# --- Interfaz ---
render_header(patu_b64)
render_sidebar()
render_historial(patu_avatar_url)
handle_chat_input(patu_avatar_url)
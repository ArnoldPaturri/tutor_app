"""Barra lateral: botón de reinicio y carga de imágenes."""

import streamlit as st

from config import TIPOS_IMAGEN_PERMITIDOS
from ui.state import reiniciar_conversacion


def render_sidebar() -> None:
    """Dibuja la barra lateral y actualiza session_state.imagen_pendiente si se sube un archivo."""
    with st.sidebar:
        st.header("⚙️ Configuración")

        if st.button("🗑️ Reiniciar conversación", use_container_width=True):
            reiniciar_conversacion()
            st.rerun()

        st.divider()

        st.subheader("📷 Adjuntar imagen")
        st.markdown(
            "<p style='font-size: 0.9rem;'>Sube una captura de tu error o código para que Patu la analice.</p>",
            unsafe_allow_html=True,
        )

        imagen_subida = st.file_uploader(
            label="Subir captura",
            type=TIPOS_IMAGEN_PERMITIDOS,
            label_visibility="collapsed",
        )

        if imagen_subida is not None:
            st.session_state.imagen_pendiente = imagen_subida
            st.image(imagen_subida, caption="📸 Imagen lista", use_container_width=True)

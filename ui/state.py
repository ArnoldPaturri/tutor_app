"""Inicialización del session_state. Un solo lugar para saber qué claves existen."""

import streamlit as st

from prompts import SYSTEM_PROMPT


def init_session_state() -> None:
    """Crea las claves de session_state si todavía no existen (primera carga de la página)."""
    if "historial" not in st.session_state:
        st.session_state.historial = [{"role": "system", "content": SYSTEM_PROMPT}]

    if "imagen_pendiente" not in st.session_state:
        st.session_state.imagen_pendiente = None


def reiniciar_conversacion() -> None:
    """Resetea el chat a su estado inicial."""
    st.session_state.historial = [{"role": "system", "content": SYSTEM_PROMPT}]
    st.session_state.imagen_pendiente = None

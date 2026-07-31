"""Renderizado del historial de chat y manejo del envío de mensajes."""

import streamlit as st

from image_utils import construir_contenido_usuario, extraer_texto_para_mostrar
from llm_client import preguntar_al_tutor_stream


def render_historial(patu_avatar_url: str) -> None:
    """Redibuja todos los mensajes guardados (se ejecuta en cada rerun de Streamlit)."""
    for mensaje in st.session_state.historial:
        if mensaje["role"] == "system":
            continue

        avatar = "👤" if mensaje["role"] == "user" else patu_avatar_url

        with st.chat_message(mensaje["role"], avatar=avatar):
            if isinstance(mensaje["content"], list):
                for bloque in mensaje["content"]:
                    if bloque.get("type") == "image_url":
                        st.image(bloque["image_url"]["url"])
            st.markdown(extraer_texto_para_mostrar(mensaje["content"]))


def handle_chat_input(patu_avatar_url: str) -> None:
    """
    Muestra el chat_input y, si el usuario escribe algo:
    1. arma y guarda su mensaje (con imagen adjunta si hay una pendiente),
    2. pide la respuesta al modelo en streaming,
    3. guarda la respuesta en el historial.
    """
    mensaje_usuario = st.chat_input("Escribe tu código, error o pregunta...")
    if not mensaje_usuario:
        return

    imagen_actual = st.session_state.imagen_pendiente
    contenido_usuario = construir_contenido_usuario(mensaje_usuario, imagen_actual)

    # Guardar y mostrar el mensaje del usuario
    st.session_state.historial.append({"role": "user", "content": contenido_usuario})
    with st.chat_message("user", avatar="👤"):
        if imagen_actual is not None:
            st.image(imagen_actual)
        st.markdown(mensaje_usuario)

    # La imagen ya quedó adjunta a este mensaje: limpiamos el estado pendiente
    st.session_state.imagen_pendiente = None

    # Generar y mostrar la respuesta del tutor en streaming
    with st.chat_message("assistant", avatar=patu_avatar_url):
        respuesta_completa = st.write_stream(
            preguntar_al_tutor_stream(st.session_state.historial)
        )

    if respuesta_completa:
        st.session_state.historial.append({"role": "assistant", "content": respuesta_completa})
        # Rerun para que el file_uploader del sidebar se limpie visualmente
        st.rerun()

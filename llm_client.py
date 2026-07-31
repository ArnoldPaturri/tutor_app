"""Todo lo relacionado a la comunicación con el modelo vive aquí."""

import streamlit as st
from openai import OpenAI

from config import LM_STUDIO_BASE_URL, LM_STUDIO_API_KEY, MODELO, TEMPERATURE


@st.cache_resource
def get_client() -> OpenAI:
    """
    Crea el cliente una sola vez y lo reutiliza entre reruns de Streamlit.
    @st.cache_resource evita reabrir una conexión nueva en cada interacción del usuario.
    """
    return OpenAI(base_url=LM_STUDIO_BASE_URL, api_key=LM_STUDIO_API_KEY)


def preguntar_al_tutor_stream(historial: list[dict]):
    """
    Generador que produce fragmentos de texto a medida que el modelo responde.
    Pensado para usarse directamente con st.write_stream(...).
    """
    cliente = get_client()
    try:
        stream = cliente.chat.completions.create(
            model=MODELO,
            messages=historial,
            temperature=TEMPERATURE,
            stream=True,
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content
            if content is not None:
                yield content
    except Exception as e:
        # Mostramos el error en la UI y detenemos el generador limpiamente.
        st.error(f"⚠️ Error de conexión con el modelo local: {e}", icon="⚠️")
        return

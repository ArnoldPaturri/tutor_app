"""Encabezado principal de la app (título + mascota)."""

import streamlit as st


def render_header(patu_b64: str | None) -> None:
    """Dibuja el encabezado con la imagen de Patu (o un emoji de respaldo si no hay imagen)."""
    if patu_b64:
        imagen_html = f'<img src="data:image/png;base64,{patu_b64}" class="header-patu-img">'
    else:
        imagen_html = (
            '<div class="header-patu-img" style="display:flex; align-items:center; '
            'justify-content:center; font-size:3rem; background:#161b22;">🦆</div>'
        )

    st.markdown(
        f"""
        <div class="header-container">
            {imagen_html}
            <div class="header-text-container">
                <h1 class="header-title">Tutor de Programación</h1>
                <p class="header-caption">Pregunta al Prof. Paturri sobre código o errores. ¡Estoy aquí para ayudarte!</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

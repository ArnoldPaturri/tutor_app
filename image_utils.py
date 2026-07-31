"""
Funciones puras de conversión de imágenes.
No dependen de Streamlit: reciben datos y devuelven datos.
Esto las hace fáciles de reutilizar y de probar con pytest si algún día quieres tests.
"""

import base64
import os


def cargar_imagen_local_base64(path: str) -> str | None:
    """Lee un archivo de imagen del disco y lo devuelve como string base64 puro."""
    if not os.path.exists(path):
        return None
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def imagen_a_data_url(archivo_subido, b64: str | None = None, mime: str | None = None) -> str:
    """
    Construye un data URL (data:image/png;base64,...) a partir de:
    - un archivo subido por st.file_uploader, o
    - un base64 y mime type ya calculados (para la mascota, por ejemplo).
    """
    if archivo_subido is not None:
        bytes_imagen = archivo_subido.getvalue()
        b64 = base64.b64encode(bytes_imagen).decode("utf-8")
        mime = archivo_subido.type
    return f"data:{mime};base64,{b64}"


def extraer_texto_para_mostrar(contenido) -> str:
    """
    El campo 'content' de un mensaje puede ser:
    - un string simple (solo texto), o
    - una lista de bloques (texto + imagen) cuando se adjunta una foto.
    Esta función siempre devuelve solo el texto, para mostrarlo en el chat.
    """
    if isinstance(contenido, str):
        return contenido
    for bloque in contenido:
        if bloque.get("type") == "text":
            return bloque.get("text", "")
    return ""


def construir_contenido_usuario(texto: str, archivo_imagen=None):
    """
    Arma el 'content' que se guarda en el historial para un mensaje del usuario.
    Si hay imagen, devuelve una lista multimodal; si no, devuelve el texto plano.
    """
    if archivo_imagen is None:
        return texto
    return [
        {"type": "text", "text": texto},
        {"type": "image_url", "image_url": {"url": imagen_a_data_url(archivo_imagen)}},
    ]

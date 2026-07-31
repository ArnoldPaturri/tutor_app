"""
Configuración centralizada de la app.
Si cambias de modelo, de servidor LM Studio, o de mascota,
este es el ÚNICO archivo que necesitas tocar.
"""

# --- Metadatos de la página ---
APP_TITLE = "Tutor de Programación | Prof. Paturri"
APP_ICON = "🦆"

# --- Conexión al LLM local (LM Studio) ---
LM_STUDIO_BASE_URL = "http://127.0.0.1:1234/v1"
LM_STUDIO_API_KEY = "lm-studio"
MODELO = "google/gemma-4-e2b"  # Ajusta al nombre exacto que muestra LM Studio
TEMPERATURE = 0.2

# --- Recursos visuales ---
PATH_IMAGEN_MASCOTA = "assets/patu.png"
NOMBRE_MASCOTA = "Patu"

# --- Tipos de imagen permitidos para adjuntar en el chat ---
TIPOS_IMAGEN_PERMITIDOS = ["png", "jpg", "jpeg", "webp"]

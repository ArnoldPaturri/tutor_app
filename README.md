# 🦆 Tutor de Programación — Prof. Paturri

Chatbot educativo construido con **Streamlit** que corre 100% en local usando **LM Studio** como servidor de inferencia. Prof. Paturri ayuda a estudiantes principiantes a entender código, depurar errores y aprender buenas prácticas de programación, con soporte para adjuntar capturas de pantalla (imágenes) cuando el modelo cargado soporta visión.

¿Por qué se creó? Como estudiante me pasa mucho que realizo consultas  a la IA para solucionar errores de codigo u
otros inconvenientes y me llega pasar que me quedo sin créditos, entonces decidí crear esto para que me ayude a
resolver problemas de programación sin que se me agoten los créditos. Básicamente es un consultor ilimitado, 
considero que cualquier estudiante puede copiarlo y hacerlo correr de manera local y apoyarse en su día a día.

## ✨ Características

- 💬 Interfaz de chat con streaming de respuestas en tiempo real.
- 📷 Soporte para adjuntar imágenes (capturas de error, código, diagramas) a modelos multimodales.
- 🎨 Interfaz oscura personalizada con CSS propio.
- 🧩 Arquitectura modular: cada responsabilidad vive en su propio archivo.
- 🔒 100% local y privado: tu código y tus conversaciones nunca salen de tu máquina (siempre que uses LM Studio local).

## 📁 Estructura del proyecto

```
tutor_app/
├── app.py              # Punto de entrada — orquesta todos los módulos
├── config.py            # Configuración: URLs, modelo, rutas, constantes
├── prompts.py            # System prompt del tutor (personalidad y reglas)
├── styles.py             # CSS de la interfaz
├── llm_client.py          # Cliente OpenAI-compatible + función de streaming
├── image_utils.py          # Conversión de imágenes a base64 / data URLs
├── requirements.txt        # Dependencias del proyecto
├── assets/
│   └── patu.png           # Avatar/mascota del tutor (debes agregarlo tú)
└── ui/
    ├── __init__.py
    ├── state.py            # Inicialización de session_state
    ├── header.py            # Encabezado con la mascota
    ├── sidebar.py            # Barra lateral (reset + subida de imágenes)
    └── chat.py              # Historial de chat + manejo de envío de mensajes
```

## 🔧 Requisitos previos

- **Python 3.10 o superior** (el proyecto usa sintaxis de type hints tipo `str | None`).
- **[LM Studio](https://lmstudio.ai/)** instalado y corriendo localmente.
- Un modelo cargado en LM Studio con el servidor local activo (por defecto en `http://127.0.0.1:1234`).
  - Para usar la función de imágenes, el modelo debe ser **multimodal** (ej. familia Gemma 3, Qwen2-VL, LLaVA). Modelos de solo texto (como Gemma 2) rechazarán las imágenes con un error.

## 🚀 Instalación

1. Clona o descarga este proyecto.
2. (Recomendado) Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # En Windows: venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Coloca tu imagen de mascota en `assets/patu.png` (opcional — si no existe, se usa un emoji 🦆 de respaldo).

## ▶️ Uso

1. Abre LM Studio, carga tu modelo y activa el servidor local (pestaña "Local Server" → "Start Server").
2. Verifica que la URL y el puerto coincidan con los de `config.py` (por defecto `http://127.0.0.1:1234/v1`).
3. Corre la app:
   ```bash
   streamlit run app.py
   ```
4. Se abrirá automáticamente en tu navegador (normalmente en `http://localhost:8501`).
5. Escribe tu pregunta, pega tu código o error, y opcionalmente adjunta una captura de pantalla desde la barra lateral antes de enviar tu mensaje.

## ⚙️ Configuración

Toda la configuración editable vive en `config.py`:

| Variable | Descripción | Valor por defecto |
|---|---|---|
| `LM_STUDIO_BASE_URL` | URL del servidor local de LM Studio | `http://127.0.0.1:1234/v1` |
| `MODELO` | Nombre exacto del modelo cargado en LM Studio | `google/gemma-4-e2b` |
| `TEMPERATURE` | Creatividad de las respuestas (0 = más determinista) | `0.2` |
| `PATH_IMAGEN_MASCOTA` | Ruta al avatar del tutor | `assets/patu.png` |
| `TIPOS_IMAGEN_PERMITIDOS` | Formatos de imagen aceptados para adjuntar | `png, jpg, jpeg, webp` |

Para editar la personalidad o las reglas del tutor, modifica `prompts.py`.

## 🐛 Solución de problemas

**"Error de conexión con el modelo local"**
Verifica que LM Studio esté abierto, el modelo cargado, y el servidor local iniciado en el puerto configurado en `config.py`.

**El modelo rechaza las imágenes**
El modelo cargado no soporta visión. Cambia a uno multimodal (ej. Gemma 3) en LM Studio y actualiza `MODELO` en `config.py` con el nombre exacto que muestra LM Studio.

**No aparece la mascota / se ve un emoji 🦆 en su lugar**
Asegúrate de que el archivo exista exactamente en `assets/patu.png`. Si el archivo no existe, la app usa automáticamente el emoji de respaldo sin fallar.

## 📄 Licencia

Proyecto de uso personal/educativo. Ajusta esta sección si planeas publicarlo o compartirlo.

"""CSS de la aplicación, aislado del resto de la lógica."""

import streamlit as st

_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

    :root {
        --bg-color-main: #0e1117;
        --bg-color-secondary: #161b22;
        --bg-color-chat-user: #1c2128;
        --border-color: #30363d;
        --text-color-main: #c9d1d9;
        --text-color-bright: #ffffff;
        --accent-color: #1f6feb;
        --font-family: 'Inter', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    .stApp {
        background-color: var(--bg-color-main);
        color: var(--text-color-main);
        font-family: var(--font-family);
    }

    [data-testid="stSidebar"] {
        background-color: var(--bg-color-secondary);
        border-right: 1px solid var(--border-color);
    }

    [data-testid="stSidebar"] .stMarkdown h2, [data-testid="stSidebar"] .stMarkdown h3 {
        color: var(--text-color-bright);
        font-weight: 600;
    }

    [data-testid="stSidebar"] p {
        color: #8b949e;
    }

    [data-testid="stSidebar"] button {
        background-color: var(--bg-color-main);
        color: var(--text-color-bright);
        border: 1px solid var(--border-color);
        border-radius: 6px;
        transition: all 0.2s;
    }
    [data-testid="stSidebar"] button:hover {
        border-color: #8b949e;
        background-color: #1c2128;
    }

    .header-container {
        display: flex;
        align-items: center;
        gap: 20px;
        padding-bottom: 25px;
        border-bottom: 1px solid var(--border-color);
        margin-bottom: 30px;
    }

    .header-patu-img {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid var(--accent-color);
        box-shadow: 0 0 15px rgba(31, 111, 235, 0.3);
    }

    .header-title {
        color: var(--text-color-bright);
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        line-height: 1.2;
    }

    .header-caption {
        font-size: 1rem;
        color: #8b949e;
        margin: 5px 0 0 0;
    }

    #tutor-de-programación {
        display: none;
    }

    [data-testid="stChatMessage"] {
        background-color: transparent;
        border-radius: 0;
        padding: 1.5rem 0;
        border-bottom: 1px solid var(--border-color);
    }

    [data-testid="stChatMessageUser"] {
        background-color: var(--bg-color-chat-user);
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }

    [data-testid="stChatMessage"] .stMarkdown {
        padding-left: 0.5rem;
    }

    [data-testid="stChatMessage"] .stMarkdown p {
        color: var(--text-color-main);
        line-height: 1.6;
        font-size: 1rem;
    }

    [data-testid="stChatMessageAvatarContainer"] {
        background-color: transparent;
        border: none;
    }

    [data-testid="stChatMessageAvatarImage"] {
        border-radius: 50%;
    }

    [data-testid="stChatMessage"] img {
        border-radius: 8px;
        border: 1px solid var(--border-color);
        margin-top: 10px;
    }

    code {
        color: #ff7b72;
        background-color: rgba(110, 118, 129, 0.2);
        padding: 0.2em 0.4em;
        border-radius: 6px;
        font-size: 85%;
    }

    pre {
        background-color: #161b22 !important;
        border: 1px solid var(--border-color);
        border-radius: 8px;
        padding: 16px !important;
    }

    pre code {
        color: #e6edf3 !important;
        background-color: transparent !important;
        padding: 0;
        font-size: 90%;
    }

    .stChatInputContainer {
        border-radius: 24px;
        border: 1px solid var(--border-color);
        background-color: var(--bg-color-secondary) !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }

    .stChatInputContainer textarea {
        color: var(--text-color-bright);
        background-color: transparent !important;
        font-size: 1rem;
    }
</style>
"""


def inject_css() -> None:
    """Inyecta el CSS personalizado en la página. Llamar una vez al inicio de app.py."""
    st.markdown(_CSS, unsafe_allow_html=True)

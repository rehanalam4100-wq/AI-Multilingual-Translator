import streamlit as st
import base64
import json
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    pipeline
)


# ============================================================
# PROFESSIONAL BACKGROUND
# ============================================================

def set_background():

    with open("Translator.png", "rb") as file:
        image = base64.b64encode(file.read()).decode()

    st.markdown(
        f"""
        <style>

        /* ================================
           FULL SCREEN BACKGROUND
           ================================ */

        .stApp {{
            background-image: url("data:image/png;base64,{image}") !important;
            background-size: cover !important;
            background-position: center center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;

            /* IMPORTANT: DO NOT USE opacity here */
            opacity: 1 !important;
        }}


        /* Keep Streamlit areas transparent */
        [data-testid="stAppViewContainer"] {{
            background: transparent !important;
        }}

        [data-testid="stHeader"] {{
            background: transparent !important;
        }}


        /* ================================
           KEEP MAIN INTERFACE FULLY VISIBLE
           ================================ */

        .main {{
            background: transparent !important;
            opacity: 1 !important;
        }}

        .block-container {{
            background: transparent !important;
            opacity: 1 !important;
            position: relative !important;
            z-index: 2 !important;
        }}


        /* ================================
           INPUT BOXES
           ================================ */

        textarea {{
            opacity: 1 !important;
            background-color: rgba(10, 25, 55, 0.92) !important;
            color: white !important;
        }}

        input {{
            opacity: 1 !important;
        }}


        /* ================================
           DROPDOWN
           ================================ */

        [data-baseweb="select"] {{
            opacity: 1 !important;
        }}


        /* ================================
           BUTTONS
           ================================ */

        button {{
            opacity: 1 !important;
        }}


        /* ================================
           REMOVE DEFAULT STREAMLIT UI
           ================================ */

        #MainMenu {{
            visibility: hidden;
        }}

        footer {{
            visibility: hidden;
        }}

        header {{
            background: transparent !important;
        }}


        /* ================================
           SCROLLBAR
           ================================ */

        ::-webkit-scrollbar {{
            width: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: transparent;
        }}

        ::-webkit-scrollbar-thumb {{
            background: rgba(80, 160, 255, 0.5);
            border-radius: 10px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


set_background()


# ============================================================
# YOUR EXISTING TRANSLATOR CODE STARTS HERE
# ============================================================

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

# KEEP THE REST OF YOUR EXISTING CODE BELOW


# ==============================
# YOUR TRANSLATOR CODE
# ==============================

translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

# YOUR EXISTING CODE CONTINUES HERE...


# YOUR TRANSLATOR CODE BELOW
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

# rest of your code...


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI Multilingual Translator",
    page_icon="🌍",
    layout="wide"
)


# ==========================================
# LOAD CSS
# ==========================================

with open("style.css", "r", encoding="utf-8") as f:
    st.markdown(
        "<style>" + f.read() + "</style>",
        unsafe_allow_html=True
    )


# ==========================================
# LOAD AI TRANSLATION MODEL
# ==========================================

@st.cache_resource
def load_translator():

    translator = pipeline(
        "translation",
        model="facebook/nllb-200-distilled-600M",
        device=-1
    )

    return translator
# ==========================================
# LOAD LANGUAGE DATA
# ==========================================

with open("language.json", "r", encoding="utf-8") as f:
    languages = json.load(f)


def get_language_code(language):

    for item in languages:

        if item["Language"].lower() == language.lower():
            return item["FLORES-200 code"]

    return None


# ==========================================
# HEADER
# ==========================================

st.markdown(
    """
    # 🧠 AI Multilingual Translator
    ### 🌍 Break language barriers with Artificial Intelligence
    """
)


st.markdown(
    """
    **🌐 200+ Languages** &nbsp;&nbsp; 
    **🧠 AI Powered** &nbsp;&nbsp; 
    **⚡ NLLB-200** &nbsp;&nbsp; 
    **🔒 Simple & Secure**
    """
)


st.divider()


# ==========================================
# MAIN TRANSLATOR
# ==========================================

st.subheader("✨ AI Translation Workspace")


col1, col2 = st.columns(2)


# ==========================================
# INPUT
# ==========================================

with col1:

    st.markdown("### 📝 English Text")

    text = st.text_area(
        "Enter your text",
        placeholder="Type something in English...",
        height=220,
        label_visibility="collapsed"
    )


# ==========================================
# LANGUAGE
# ==========================================

with col2:

    st.markdown("### 🌐 Destination Language")

    language = st.selectbox(
        "Select language",
        [
            "German",
            "French",
            "Hindi",
            "Telugu"
        ],
        label_visibility="collapsed"
    )

    st.info(
        "🤖 NLLB-200 will translate your English text "
        "into the selected language."
    )


# ==========================================
# TRANSLATE BUTTON
# ==========================================

st.markdown("")


if st.button("🌐 TRANSLATE", use_container_width=True):

    translator = load_translator()

    if not text.strip():

        st.warning("⚠️ Please enter some English text.")

    else:

        code = get_language_code(language)

        if code is None:

            st.error("Language code not found.")

        else:

            with st.spinner("🤖 AI is translating..."):

                result = translator(
                    text,
                    src_lang="eng_Latn",
                    tgt_lang=code
                )

            translated = result[0]["translation_text"]

            st.success("✅ Translation Complete")

            st.subheader("📖 Translated Text")

            st.text_area(
                "Translation",
                translated,
                height=180,
                label_visibility="collapsed"
            )


# ==========================================
# FEATURES
# ==========================================

st.divider()

st.subheader("🚀 Why Use AI Multilingual Translator?")


c1, c2, c3 = st.columns(3)


with c1:

    st.markdown("### 📚 Learn")

    st.write(
        "Understand content from different languages "
        "and explore new cultures."
    )


with c2:

    st.markdown("### 👥 Communicate")

    st.write(
        "Connect with people around the world "
        "without language barriers."
    )


with c3:

    st.markdown("### 🌐 Grow")

    st.write(
        "Make information more accessible "
        "across different languages."
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Made with ❤️ for a Connected World  |  "
    "Powered by NLLB-200"
)

import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from io import BytesIO

# ---------------- Page Configuration ----------------

st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)


# ---------------- Title ----------------

st.title("🌍 AI Language Translation Tool")
st.write("Translate text into multiple languages instantly.")

# ---------------- Language Dictionaries ----------------

translator_languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

tts_languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN",
    "Arabic": "ar"
}

# ---------------- Session State ----------------

if "history" not in st.session_state:
    st.session_state.history = []

if "source" not in st.session_state:
    st.session_state.source = "Auto Detect"

if "target" not in st.session_state:
    st.session_state.target = "Tamil"

# ---------------- Input ----------------

text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type your text here..."
)

# ---------------- Language Selection ----------------

col1, col2, col3 = st.columns([4,1,4])

with col1:

    source = st.selectbox(
        "Source Language",
        list(translator_languages.keys()),
        index=list(translator_languages.keys()).index(
            st.session_state.source
        )
    )

with col2:

    st.write("")
    st.write("")

    if st.button("🔄"):

        if source != "Auto Detect":

            temp = st.session_state.source
            st.session_state.source = st.session_state.target
            st.session_state.target = temp

            st.rerun()

with col3:

    target = st.selectbox(
        "Target Language",
        list(tts_languages.keys()),
        index=list(tts_languages.keys()).index(
            st.session_state.target
        )
    )

st.session_state.source = source
st.session_state.target = target
# ---------------- Translate ----------------

if st.button("🌍 Translate"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        try:

            translated = GoogleTranslator(
                source=translator_languages[st.session_state.source],
                target=translator_languages[st.session_state.target]
            ).translate(text)

            st.success("✅ Translation Successful!")

            st.text_area(
                "Translated Text",
                translated,
                height=180,
                key="translated_text"
            )

            # ---------------- Save History ----------------

            st.session_state.history.append({
                "Input": text,
                "Output": translated
            })

            # ---------------- Download ----------------

            st.download_button(
                label="⬇ Download Translation",
                data=translated,
                file_name="translation.txt",
                mime="text/plain"
            )

            # ---------------- Copy ----------------

            st.code(translated)

            # ---------------- Text To Speech ----------------

            try:

                tts = gTTS(
                    text=translated,
                    lang=tts_languages[st.session_state.target]
                )

                audio_bytes = BytesIO()

                tts.write_to_fp(audio_bytes)

                audio_bytes.seek(0)

                st.subheader("🔊 Listen to Translation")

                st.audio(
                    audio_bytes.read(),
                    format="audio/mp3"
                )

            except Exception as audio_error:

                st.warning(
                    f"Audio not available for this language.\n{audio_error}"
                )

        except Exception as e:

            st.error(f"Translation Error : {e}")

# ---------------- Sidebar ----------------

st.sidebar.title("📜 Translation History")

if st.sidebar.button("🗑 Clear History"):

    st.session_state.history = []

if len(st.session_state.history) == 0:

    st.sidebar.info("No translations yet.")

else:

    for item in reversed(st.session_state.history):

        st.sidebar.markdown("### Input")
        st.sidebar.write(item["Input"])

        st.sidebar.markdown("### Output")
        st.sidebar.write(item["Output"])

        st.sidebar.markdown("---")

# ---------------- Footer ----------------

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center">
        <h4>🌍 AI Language Translation Tool</h4>
        <p>
        Developed by <b>Menil Sri</b><br>
        CodeAlpha Artificial Intelligence Internship 2026
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
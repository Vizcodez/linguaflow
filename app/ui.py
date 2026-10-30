
import streamlit as st
import tempfile
from pathlib import Path

from speech import transcribe_audio
#from translation import translate


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="LinguaFlow",
    page_icon="🌐",
    layout="centered"
)


# -----------------------------
# Application heading
# -----------------------------
st.title("🌐 LinguaFlow")
st.caption("Your voice, understood across languages.")

st.divider()


# -----------------------------
# Language selection
# -----------------------------
st.subheader("🌍 Choose your languages")

col1, col2 = st.columns(2)

with col1:
    st.selectbox(
        "Translate from",
        ["Malayalam"],
        key="source_language"
    )

with col2:
    st.selectbox(
        "Translate to",
        ["English"],
        key="target_language"
    )

st.caption("More language pairs will be added later.")

st.divider()


# -----------------------------
# Audio upload
# -----------------------------
st.subheader("🎤 Your voice")

audio_file = st.file_uploader(
    "Upload an audio recording",
    type=["wav", "mp3", "m4a", "ogg", "flac"]
)

if audio_file is not None:
    st.audio(audio_file)


# -----------------------------
# Transcription and translation
# -----------------------------
if st.button("✨ Translate", use_container_width=True):

    if audio_file is None:
        st.warning("Please upload an audio recording first.")

    else:
        temp_audio_path = None

        try:
            # Save the uploaded audio temporarily
            suffix = Path(audio_file.name).suffix or ".wav"

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix
            ) as temp_audio:
                temp_audio.write(audio_file.getvalue())
                temp_audio_path = temp_audio.name

            # Step 1: Recognize speech
            with st.spinner("🎧 Recognizing your speech..."):
                recognized_text, detected_language = (
                    transcribe_audio(temp_audio_path)
                )

            if not recognized_text.strip():
                st.warning(
                    "No speech was recognized. "
                    "Try a clearer audio recording."
                )

            else:
                st.success(
                    f"Speech recognition complete! "
                    f"Detected language: {detected_language}"
                )

                # Display the recognized transcript
                st.subheader("📝 Recognized speech")

                st.text_area(
                    "Original transcript",
                    value=recognized_text,
                    height=140,
                    disabled=True
                )

                # Step 2: Translate Malayalam to English
                
                # Whisper already attempts to translate the speech into English
                st.subheader("🌍 English translation")

                st.text_area(
                    "Translated text",
                    value=recognized_text,
                    height=140,
                    disabled=True
                )

                st.success("Translation attempt complete!")

        except Exception as error:
            st.error(
                "Something went wrong while processing the audio."
            )
            st.exception(error)

        finally:
            # Remove the temporary audio file
            if temp_audio_path is not None:
                Path(temp_audio_path).unlink(missing_ok=True)


# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption(
    "LinguaFlow • AI-powered multilingual speech translation"
)

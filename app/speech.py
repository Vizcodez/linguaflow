import whisper

print("Loading Whisper model...")

model = whisper.load_model("base")



def transcribe_audio(audio_path):
    """
    Convert Malayalam speech directly into English text.
    """
    result = model.transcribe(
        audio_path,
        language="ml",
        task="translate",
        temperature=0,
        condition_on_previous_text=False,
        fp16=False
    )

    return result["text"], result["language"]

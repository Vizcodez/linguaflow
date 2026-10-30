from speech import transcribe_audio
from translation import translate

AUDIO_FILE = "D:/LinguaFlow/data/mm_clean.wav"

print("Transcribing audio...")

text, language = transcribe_audio(AUDIO_FILE)

print("\nDetected Language:", language)

print("\nRecognized Text:")
print(text)

# For our first integration test,
# we know the audio is Malayalam.
if language == "ml":
    source_language = "mal_Mlym"
    target_language = "hin_Deva"

    print("\nTranslating to Hindi...")

    translated_text = translate(
        text,
        source_language,
        target_language
    )

    print("\nHindi Translation:")
    print(translated_text)

else:
    print("\nThis test is configured for Malayalam audio.")
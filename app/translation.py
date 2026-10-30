import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from IndicTransToolkit import IndicProcessor

MODEL_NAME = "ai4bharat/indictrans2-indic-en-dist-200M"

# Use CPU for now
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading translation model...")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True
).to(DEVICE)

processor = IndicProcessor(inference=True)

print("Translation model loaded successfully!")


def translate(text, source_language, target_language):

    # Prepare the input
    batch = processor.preprocess_batch(
        [text],
        src_lang=source_language,
        tgt_lang=target_language
    )

    # Convert text into model inputs
    inputs = tokenizer(
        batch,
        truncation=True,
        padding="longest",
        return_tensors="pt",
        return_attention_mask=True
    ).to(DEVICE)

    # Generate translation
    with torch.no_grad():
        generated_tokens = model.generate(
            **inputs,
            use_cache=True,
            min_length=0,
            max_length=256,
            num_beams=5,
            num_return_sequences=1
        )

    # Convert model output back to text
    generated_tokens = tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=True
    )

    translations = processor.postprocess_batch(
        generated_tokens,
        lang=target_language
    )

    return translations[0]



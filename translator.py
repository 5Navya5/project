# translator.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def translate_text(text, model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=40, num_beams=4, early_stopping=True)

    translated_text = tokenizer.decode(outputs[0])
    return translated_text
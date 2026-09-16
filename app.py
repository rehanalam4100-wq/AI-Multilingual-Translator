import torch
import gradio as gr
import json
from transformers import pipeline

# Load translation model
translator = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M"
)

# Load language data
with open("language.json", "r", encoding="utf-8") as file:
    language_data = json.load(file)


# Find FLORES language code
def get_code(language):
    for item in language_data:
        if item["Language"].lower() == language.lower():
            return item["FLORES-200 code"]
    return None


# Translation function
def translate_text(text, destination_language):

    if not text:
        return "Please enter some text."

    code = get_code(destination_language)

    result = translator(
        text,
        src_lang="eng_Latn",
        tgt_lang=code
    )

    return result[0]["translation_text"]


# Create interface
demo = gr.Interface(
    fn=translate_text,

    inputs=[
        gr.Textbox(
            label="Enter English Text",
            lines=6,
            placeholder="Type something in English..."
        ),

        gr.Dropdown(
            ["German", "French", "Hindi", "Telugu"],
            label="Select Destination Language"
        )
    ],

    outputs=gr.Textbox(
        label="Translated Text",
        lines=4
    ),

    title="🌍 AI Multilingual Translator",

    description="Translate English text into multiple languages using NLLB-200."
)


demo.launch()
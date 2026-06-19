---
title: GPT-2 Text Generator
emoji: 🤗
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.1"
python_version: "3.10"
app_file: app.py
pinned: false
---

# GPT-2 Text Generator

This Hugging Face Space uses a pretrained GPT-2 model from the Transformers library to generate meaningful text from a user prompt.

## Features

- Gradio web interface.
- Pretrained GPT-2 text generation.
- Output trimmed to about 250 words.
- Easy to run on Hugging Face Spaces.

## Files

- `app.py`
- `requirements.txt`

## Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python app.py
```

## Notes

The app uses `max_new_tokens=250` and trims the output to 250 words after generation to keep the response within your requested limit.
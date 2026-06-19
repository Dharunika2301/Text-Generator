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

This Space uses a pretrained GPT-2 model from Hugging Face Transformers to generate meaningful text from a prompt.

## Features

- Gradio web interface.
- GPT-style text generation.
- Output limited to about 250 words.
- Works on Hugging Face Spaces.

## How it works

The app uses `max_new_tokens=250` for generation, then trims the output to 250 words so the response stays within your requested limit.

## Files

- `app.py`
- `requirements.txt`

## Run locally

```bash
pip install -r requirements.txt
python app.py
```
---
title: GPT Text Generator
emoji: 🤗
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.1"
python_version: "3.10"
app_file: app.py
pinned: false
---

# GPT Text Generator

This app generates text from a user prompt using a pretrained GPT model from Hugging Face Transformers.

## Features

- Enter any prompt.
- Generate up to 250 new tokens.
- Display the generated text in the app.

## How it works

The app uses a GPT-style causal language model and the Hugging Face `text-generation` pipeline. For GPT-2 style models, setting the pad token to the EOS token helps avoid padding warnings [web:13][web:16].

## Files

- `app.py` - main application file.
- `requirements.txt` - Python dependencies.

## Installation

```bash
pip install -r requirements.txt
```

## Run locally

```bash
python app.py
```

## Hugging Face Space notes

Make sure `app_file: app.py` matches your actual file name, and keep the YAML block at the very top of the README. Hugging Face Spaces reads this metadata directly from `README.md` [web:42][web:44].

## Example prompt

```text
What is the importance of recycling?
```
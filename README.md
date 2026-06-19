---
title: GPT Text Generator
emoji: 🤗
colorFrom: blue
colorTo: green
sdk: docker
sdk_version: "latest"
python_version: "3.10"
app_file: app.py
pinned: false
---

# GPT Text Generator

A Flask app on Hugging Face Spaces that generates meaningful text from a user prompt using a pretrained GPT model from the Hugging Face Transformers library.

## Features

- Enter a prompt.
- Generate text with a pretrained GPT model.
- Limit output to about 250 words.
- Simple web interface.

## Files

- `app.py` — main Flask application.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — needed for Docker Spaces.

## How it works

The app uses the Hugging Face `text-generation` pipeline with `gpt2`. It generates up to 250 new tokens and then trims the final response to 250 words.

## Install locally

```bash
pip install -r requirements.txt
```

## Run locally

```bash
python app.py
```

## Hugging Face Spaces note

This Space is configured as a Docker Space, so the app should listen on port 7860 and use `app.py` as the main file.

## Example prompt

```text
What is the importance of recycling?
```
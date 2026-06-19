

# GPT Text Generator

This is a simple Flask web application that uses a pretrained GPT model from the Hugging Face Transformers library to generate text from a user prompt.

## Features

- Enter a prompt in a web form.
- Generate text using a pretrained GPT model.
- Display the generated output in the browser.
- Supports up to 250 generated tokens.

## Requirements

- Python 3.10 or later
- Flask
- Transformers
- PyTorch
- SentencePiece

## Installation

1. Clone this repository or download the files.
2. Open a terminal in the project folder.
3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Project Files

- `app.py` — Main Flask application.
- `requirements.txt` — Python dependencies.
- `templates/` — Optional folder for HTML templates if you move HTML out of `app.py`.

## Run the App

Start the application with:

```bash
python app.py
```

Then open your browser and go to:

```bash
http://127.0.0.1:5000
```

## How It Works

- The user enters a prompt in the text box.
- The app sends the prompt to a pretrained GPT model.
- The model generates text using `max_new_tokens=250`.
- The generated text is shown on the page.

## Notes

- `max_new_tokens=250` limits the model to generating up to 250 new tokens.
- If you want exactly 250 words, you may need extra word-trimming logic after generation.
- If you see warnings about padding, the app sets the pad token to the EOS token for GPT-style models.

## Example Prompt

```text
What is the importance of recycling?
```

## Example Output

The output will vary each time because the model generates text probabilistically.

## License

This project is for learning and demonstration purposes.

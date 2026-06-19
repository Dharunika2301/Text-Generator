import os
from flask import Flask, request, render_template_string
from transformers import pipeline

app = Flask(__name__)

generator = pipeline("text-generation", model="gpt2")

if generator.tokenizer.pad_token is None:
    generator.tokenizer.pad_token = generator.tokenizer.eos_token

HTML = """
<!doctype html>
<html>
<head>
    <title>GPT Text Generator</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <h2>GPT Text Generator</h2>
    <form method="post">
        <input type="text" name="prompt" style="width: 420px;" placeholder="Enter your prompt" required>
        <button type="submit">Generate</button>
    </form>
    {% if generated_text %}
        <h3>Generated Text</h3>
        <p>{{ generated_text }}</p>
    {% endif %}
</body>
</html>
"""

def limit_to_250_words(text):
    words = text.split()
    return " ".join(words[:250])

@app.route("/", methods=["GET", "POST"])
def home():
    generated_text = ""
    if request.method == "POST":
        prompt = request.form["prompt"].strip()
        result = generator(
            prompt,
            max_new_tokens=250,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            num_return_sequences=1,
            pad_token_id=generator.tokenizer.eos_token_id,
        )
        generated_text = limit_to_250_words(result[0]["generated_text"])
    return render_template_string(HTML, generated_text=generated_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=False)
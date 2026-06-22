from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

generator = pipeline(
    "text-generation",
    model="gpt2"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json(silent=True) or {}
    prompt = data.get('prompt', '').strip()

    if not prompt:
        return jsonify({'error': 'Prompt is required.'}), 400

    result = generator(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7
    )

    return jsonify({'generated_text': result[0]['generated_text']})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860, debug=True)
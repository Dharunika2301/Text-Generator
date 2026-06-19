import gradio as gr
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_text(prompt):
    result = generator(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]

iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=5, label="Prompt"),
    outputs=gr.Textbox(lines=10, label="Generated Text"),
    title="GPT-2 Text Generator"
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0")
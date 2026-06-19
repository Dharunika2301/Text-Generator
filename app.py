import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

if generator.tokenizer.pad_token is None:
    generator.tokenizer.pad_token = generator.tokenizer.eos_token

def generate_text(prompt):
    result = generator(
        prompt,
        max_new_tokens=250,
        do_sample=True,
        temperature=0.7,
        top_p=0.95,
        num_return_sequences=1,
        pad_token_id=generator.tokenizer.eos_token_id
    )
    text = result[0]["generated_text"]
    return " ".join(text.split()[:250])

iface = gr.Interface(
    fn=generate_text,
    inputs=gr.Textbox(lines=5, label="Prompt"),
    outputs=gr.Textbox(lines=12, label="Generated Text"),
    title="GPT-2 Text Generator",
    description="Generate meaningful text from a prompt using a pretrained GPT model."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
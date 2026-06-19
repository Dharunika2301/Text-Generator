from transformers import pipeline

# Create the text generation pipeline
generator = pipeline("text-generation", model="distilbert/distilgpt2")

# Your prompt
prompt = "What is the importance of recycling?"

# Generate meaningful text
result = generator(prompt, max_length=150, num_return_sequences=1)

# Print the generated text
print(result[0]['generated_text'])
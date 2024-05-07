from fastapi import FastAPI, Body
import transformers
import torch

# Replace with a random seed value
seed_value = 42  # Example seed

torch.manual_seed(seed_value)

# Initialize tokenizer and model (using AutoModelForCausalLM)
tokenizer = transformers.AutoTokenizer.from_pretrained("gpt2")
model = transformers.AutoModelForCausalLM.from_pretrained("gpt2")
print("Model loaded successfully!")

app = FastAPI()

@app.post("/generate-poem")
async def generate_poem(prompt: str = Body(...)):
    """
    Generates a poem based on the provided prompt.
    """

    try:
        # Tokenize the prompt
        input_ids = tokenizer.encode(prompt, return_tensors="pt")

        # Generate text with GPT model
        output = model.generate(input_ids, max_length=50)  # Adjust max_length as needed

        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        return {"poem": generated_text}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("poem_generator:app", host="localhost", port=8000)  # Expose for local testing

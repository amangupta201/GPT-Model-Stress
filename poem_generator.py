import logging
import transformers
import torch
import threading

# Configure logging to display output in the console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

seed_value = 42  # Example seed

torch.manual_seed(seed_value)

# Initialize tokenizer and model (using AutoModelForCausalLM)
tokenizer = transformers.AutoTokenizer.from_pretrained("gpt2")
model = transformers.AutoModelForCausalLM.from_pretrained("gpt2")
logging.info("Model loaded successfully!")


def generate_poem(prompt: str):
    """
    Generates a poem based on the provided prompt.

    Args:
        prompt (str): The starting prompt for the poem generation.

    Returns:
        str: The generated poem, or None if an error occurs.
    """

    try:
        # Tokenize the prompt
        input_ids = tokenizer.encode(prompt, return_tensors="pt")

        # Generate attention mask (all tokens attended to in this example)
        attention_mask = torch.ones_like(input_ids)

        # Generate text with GPT model
        output = model.generate(input_ids, attention_mask=attention_mask, max_length=50)

        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        logging.info(f"Generated poem: {generated_text}")
        return generated_text
    except Exception as e:
        logging.error(f"Error generating poem: {e}")
        return None


def generate_poem_wrapper(prompt):
    def generate_poem_in_thread():
        generated_poem = generate_poem(prompt)
        # Do something with the generated poem (e.g., print, log)
        print(f"Generated Poem:\n{generated_poem}")
        return generated_poem

    thread = threading.Thread(target=generate_poem_in_thread)
    thread.start()
    return thread


if __name__ == "__main__":
    # Example usage
    threads = []
    for _ in range(10):  # Simulate 10 concurrent requests
        prompt = "The sun sets on..."
        thread = generate_poem_wrapper(prompt)
        threads.append(thread)

    for thread in threads:
        thread.join()  # Wait for all threads to finish


Poem Generation with Stress Testing





This document describes the Python code for generating poems using the GPT-2 model and incorporates stress testing functionalities to evaluate the code's performance under concurrent load.






1. Libraries and Setup




The code utilizes the following libraries:

logging: Configures logging for informative output.
transformers: Provides functionalities for working with pre-trained transformer models like GPT-2.
torch: The deep learning framework used for tensor operations during poem generation.
threading (optional): Enables creating threads for simulating concurrent poem generation requests.



2. Code Structure




The code resides in the poem_gen.py file and includes the following sections:




Logging Configuration: Sets up logging to display messages at the INFO level, including timestamps, source names, severity levels, and messages.
Random Seed: Defines a seed value (seed_value) for random number generation, ensuring replicability of results.
Model Loading:


Sets the random seed using torch.manual_seed.
Loads the pre-trained GPT-2 tokenizer (transformers.AutoTokenizer.from_pretrained) for processing text into numerical representations.
Loads the pre-trained GPT-2 model (transformers.AutoModelForCausalLM.from_pretrained) for generating text based on provided prompts.
Logs a message upon successful model loading.
generate_poem Function:



Takes a string prompt (prompt) as input.
Tokenizes the prompt using the loaded tokenizer.
Creates an attention mask (set to all ones in this example, indicating all tokens are attended to).
Generates text using the model with the provided input and attention mask, setting a maximum length for the generated poem.
Decodes the generated output tokens back to human-readable text using the tokenizer.
Logs the generated poem for informational purposes.
Returns the generated poem string or None if an error occurs.



generate_poem_wrapper Function (Optional):


This function utilizes threading to simulate concurrent poem generation requests (relevant for stress testing).
It takes a string prompt (prompt) as input.
Defines a nested function generate_poem_in_thread that calls the generate_poem function with the provided prompt.
Creates a thread object (threading.Thread) targeting the generate_poem_in_thread function.
Starts the thread execution (thread.start).
Returns the created thread object.


if __name__ == "__main__": Block:
This block executes only when the script is run directly (not imported as a module).
Defines an empty list threads to store thread objects.
Uses a loop to simulate 10 concurrent poem generation requests (you can adjust this number).
Inside the loop:
Creates a sample prompt ("The sun sets on...").
Calls generate_poem_wrapper with the prompt and stores the returned thread in the threads list.
Iterates through the threads list and calls join on each thread. This ensures the main program waits for all threads to finish generating poems before exiting.



3. Running the Script

Save the code as poem_gen.py.
Open a terminal or command prompt and navigate to the directory where you saved the file.
Run the script using python poem_gen.py.
This will initiate 10 concurrent poem generation requests (using threads by default) and print the generated poems to the console.

4. Stress Testing

The generate_poem_wrapper function demonstrates a basic approach to stress testing using threading. You can modify this functionality to:

Change the number of concurrent requests simulated in the loop.
Implement more comprehensive logging or error handling within the wrapper function.
Measure and track generation times for each request.
5. Alternative Testing Approaches

Consider exploring testing frameworks like unittest or pytest for unit testing your core poem generation logic (generate_poem function) to ensure it functions as expected under various input prompts.

This documentation provides an overview of the code structure and functionalities, including the integration of stress testing using threading. Remember to adapt the stress testing aspects based on your specific requirements and desired level of performance evaluation.

import sagemaker

# Configure SageMaker session
sagemaker_session = sagemaker.Session()

# Define model image URI (where your pre-trained model is stored)
model_image_uri = "your-model-uri"  # Replace with your actual URI

# Define the model (specifying framework and entry point)
model = sagemaker.model.Model(
    image_uri=model_image_uri,
    model_data="model.tar.gz"  # Replace if your model data has a different name
)

# Define the endpoint configuration (instance type, etc.)
endpoint_config_name = "poem-generation-endpoint-config"
predictor_instance_type = "ml.t2.medium"  # You can adjust this

sagemaker.model.create_model_config(
    instance_type=predictor_instance_type,
    model_data=model,
    name=endpoint_config_name
)

# Deploy the model endpoint
endpoint_name = "poem-generation-endpoint"
predictor = model.deploy(initial_instance_count=1, endpoint_name=endpoint_name)

# Function to generate poem using the deployed endpoint
def generate_poem(prompt):
    response = predictor.predict(prompt)
    generated_poem = response.decode("utf-8")
    return generated_poem

# Example usage (optional)
if __name__ == "__main__":
    prompt = "The sun sets on..."
    generated_poem = generate_poem(prompt)
    print(f"Generated Poem:\n{generated_poem}")

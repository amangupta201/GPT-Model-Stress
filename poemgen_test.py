import random

from fuzzywuzzy import fuzz
from locust import HttpUser, task, between

from poem_generator import generate_poem


class PoemGeneratorUser(HttpUser):
    wait_time = between(1, 5)  # Adjust wait time between requests


    mock_data = [
        {"prompt": "Once upon a time...", "poem": "A brave knight set out on a quest..."},
        # ... more examples
    ]

    @task
    def generate_poem(self):
        # Choose a random prompt from mock data
        prompt = self.mock_data[random.randint(0, len(self.mock_data) - 1)]

        # Send the prompt to your poem generation code (replace with actual call)
        generated_poem = generate_poem(prompt)

        # Verify the generated poem with fuzzy matching
        if generated_poem:
            match_ratio = fuzz.ratio(generated_poem, prompt["poem"])
            if match_ratio >= 80:  # Adjust threshold as needed
                self.log(f"Generated poem (match ratio: {match_ratio}): {generated_poem}")
            else:
                self.log(f"Generated poem with low match ratio: {generated_poem}")
                self.request.failure  # Log a failure if the match ratio is low
        else:
            self.log("Error generating poem.")
            self.request.failure


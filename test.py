from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the token from environment variables
HF_TOKEN = os.getenv("HF_TOKEN")

# Check if token loaded properly
if HF_TOKEN is None:
    raise ValueError("HF_TOKEN is not set. Make sure it's defined in your .env file.")

# Initialize client
client = InferenceClient(token=HF_TOKEN, provider="hf-inference")

# Generate text
response = client.text_generation(
    model="HuggingFaceH4/zephyr-7b-beta",
    prompt="how are you",
    max_new_tokens=50
)

print(response)

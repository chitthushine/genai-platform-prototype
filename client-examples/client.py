import requests

API_URL = "http://localhost:8000"
API_KEY = "demo123"

# Deploy a model
response = requests.post(
    f"{API_URL}/deploy", json={"model_id": "gpt2"}, headers={"X-API-Key": API_KEY}
)
print(response)

# Run inference
output = requests.post(
    f"{API_URL}/predict", json={"model_id": "gpt2", "input_text": "Hello, world!"}
).json()
print(output)

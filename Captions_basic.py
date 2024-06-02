import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "Question:can you tell me the main story behind the series Its okay to not be okay? " " Answer:",
})

print(output[0]['generated_text'])
import os
import requests
import base64

# Configuration
API_KEY = "cad6f84406c0487fb434010c83b6f142"
IMAGE_PATH = "Doggy.jpg"
encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')
headers = {
    "Content-Type": "application/json",
    "api-key": API_KEY,
}

# Payload for the request
payload = {
  "messages": [
    {
      "role": "system",
      "content": "You are a financial specialist and math expert."
    },
    {
           "role": "user",
      "content": "Please recommend one investment portflio based on"+str(top_5_tickers)+"for a person who is"+str(current_age)+ 
      "and plans to retire in"+str(years_left)+"years. Please reply the tickerl, weight, rationale."
    }
  ],
  "temperature": 0.7,
  "top_p": 0.95,
  "max_tokens": 800
}

ENDPOINT = "https://azure-openai-eastus-20240916.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-02-15-preview"

# Send request
try:
    response = requests.post(ENDPOINT, headers=headers, json=payload)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
except requests.RequestException as e:
    raise SystemExit(f"Failed to make the request. Error: {e}")

# Select the portfolio recommendation part from the reponse and print out
response_json = response.json()
portfolio_recommendation = response_json['choices'][0]['message']['content']
print(portfolio_recommendation)









import requests

API_BASE_URL = "https://api.cloudflare.com/client/v4/accounts/f3b0bf7d40c6044c021780ca8eb6ea8b/ai/run/"
headers = {"Authorization": "Bearer Yz3Fn--rHT_T71fXPLncUSep7z1nK7JdDYkNF7tF"}

def run(model, input):
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

output = run('@cf/meta/m2m100-1.2b', {
  "text": "whats my name",
  "source_lang": "english",
  "target_lang": "spanish"
})

print(output)
import requests
from secrets import API_BASE_URL, headers

def _run(model, input):
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

def translate(text: str, source_lang: str, target_lang: str):
    return _run('@cf/meta/m2m100-1.2b', {
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    })

output = _run('@cf/meta/m2m100-1.2b', {
  "text": "whats my name",
  "source_lang": "english",
  "target_lang": "spanish"
})

print(output)
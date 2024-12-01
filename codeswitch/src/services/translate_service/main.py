import requests
from db.db import TranslateLookup
from services.translate_service.secrets import API_BASE_URL, headers

def _run(model, input):
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)

    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        return response.text

def translate(text: str, source_lang: str, target_lang: str) -> str:
    # call api on text
    response = _run('@cf/meta/m2m100-1.2b', {
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang
    })

    if not response["success"]:
        raise Exception(f"Translation failed. Text: {text}. Response: ", response)
    else:
        result = response["result"]
        return result["translated_text"]

def main():
    output = _run('@cf/meta/m2m100-1.2b', {
      "text": "whats my name",
      "source_lang": "english",
      "target_lang": "spanish"
    })

    print(output)

if __name__ == "__main__":
    # main()
    print(TranslateLookup.objects())
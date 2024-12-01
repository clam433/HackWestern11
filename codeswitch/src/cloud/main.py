import os
import csv
from tqdm import tqdm
from fuzzywuzzy import process

from services.translate_service.main import translate

DATA_DIR_PATH = "../../data"
KEYWORD_DATA_PATH = DATA_DIR_PATH + "/keywords/csv"

def get_available_code_langs():
    """
    TEMP
    The final version will look into the db.
    for now just look over the folders
    """
    return [name for name in os.listdir(KEYWORD_DATA_PATH) if os.path.isdir(os.path.join(KEYWORD_DATA_PATH, name))]

def get_keywords(code_lang: str, code_version: str) -> []:
    available_langs = get_available_code_langs()

    # Use fuzzy matching to find the best match
    best_match, score = process.extractOne(code_lang, available_langs)

    if score >= 60:  # You can adjust the threshold as needed
        with open(f"{KEYWORD_DATA_PATH}/{best_match}/{code_version}/keywords.csv", "r", newline='') as f:
            csvfile = csv.reader(f)
            next(csvfile) # Skip the header
            return [keyword for row in csvfile for keyword in row] # extra loop flattens the list
    else:
        return []

def get_lang_lookup(lang, code_lang, code_version=None):
    keywords = get_keywords(code_lang, code_version)
    if not keywords:
        return {}

    result = {}
    for keyword in tqdm(keywords, unit="keyword"):
        word = translate(keyword, "en", lang)
        word = word.lower() # make it lowercase
        result[keyword] = word[:len(keyword)] # ensure brevity

    return result

if __name__ == "__main__":
    print(get_lang_lookup("french", "c++", "C++17"))
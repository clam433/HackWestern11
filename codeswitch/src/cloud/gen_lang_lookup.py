import os
import csv
from tqdm import tqdm
from fuzzywuzzy import process
from db.db import TranslateLookup, get_all_translate_tables

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

def gen_keywords(code_lang: str, code_version: str) -> []:
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
    print(f"looking up lang_to {lang}")
    # try to pull it from db
    table = TranslateLookup.objects(lang_to=lang, code_lang=code_lang, code_version=code_version).first()

    # if found, return
    if table:
        print(f"found lang_to {lang}")
        return table.translation_table
    print(f"not found lang_to {lang}")
    # if not found, generate and save
    keywords = gen_keywords(code_lang, code_version)
    if not keywords:
        raise Exception("No keywords found for the given code language and version")

    result = {}
    for keyword in tqdm(keywords, unit="keyword"):
        word = translate(keyword, "en", lang)
        word = word.lower() # make it lowercase
        result[keyword] = word[:len(keyword)] # ensure brevity

    # save to db
    table = TranslateLookup(lang_to=lang, code_lang=code_lang, code_version=code_version, translation_table=result)
    table.save()

    return result

if __name__ == "__main__":
    print(get_all_translate_tables())
    print(get_lang_lookup("french", "c++", "C++17"))
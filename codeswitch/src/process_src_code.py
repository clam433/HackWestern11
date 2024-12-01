import os

from cloud import get_lang_lookup
from db.db import get_all_translate_tables

def process_code_file(input_path: str, output_path: str, lang: str, code_lang:str, code_version: str, write=True):
    # Ensure the input file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")

    # Read the content of the input file
    with open(input_file_path, 'r') as input_file:
        content = input_file.read()

    # Process the content
    processed_content = translate_source(content, lang, code_lang, code_version)

    # Write the processed content to the output file
    if write:
        with open(output_path, 'w') as output_file:
            output_file.write(processed_content)

        print(f"Processed content has been written to {output_path}")
    else:
        print(processed_content)

def translate_source(content: str, lang: str, code_lang: str, code_version: str) -> str:
    # convert keywords
    content = _translate_keywords(content, lang, code_lang, code_version)

    # convert comments
    "nothing yet"

    return content

def _translate_keywords(content: str, lang: str, code_lang: str, code_version: str) -> str:
    # get keyword lookup
    lookup_table = get_lang_lookup(lang, code_lang, code_version)

    # replace keywords
    for keyword, translation in lookup_table.items():
        content = content.replace(keyword, translation)

    return content

if __name__ == "__main__":
    input_file_path = "../test_in/main.java"  # Change this to your input file path
    output_file_path = "../out/french.java"  # Change this to your desired output file path
    tables = get_all_translate_tables()
    print(tables)
    process_code_file(input_file_path, output_file_path, "french", "java", "SE 17 LTS", write=False)


import os
from pygments.lexers import get_lexer_by_name
from pygments.token import Token
from tqdm import tqdm

from cloud import get_lang_lookup
from services.translate_service import translate


def process_code_file(input_path: str, output_path: str, from_lang: str, to_lang: str, code_lang:str, code_version: str, write=True):
    # Ensure the input file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")

    # Read the content of the input file
    with open(input_path, 'r') as input_file:
        content = input_file.read()

    # Process the content
    processed_content = translate_source(content, from_lang, to_lang, code_lang, code_version)

    # Write the processed content to the output file
    if write:
        with open(output_path, 'w') as output_file:
            output_file.write(processed_content)

        print(f"Processed content has been written to {output_path}")
    else:
        print(processed_content)

def translate_source(content: str, from_lang: str, to_lang: str, code_lang: str, code_version: str) -> str:
    # get a lexer
    try:
        lexer = get_lexer_by_name(code_lang)
    except Exception as e:
        raise Exception(f"Could not find a lexer for {code_lang}")

    tokens = list(lexer.get_tokens(content))
    print(tokens)
    translated_content = []

    for token_type, token_value in tqdm(tokens, unit="token"):
        if token_type in Token.Punctuation or token_value == "\"":
            translated_content.append(token_value)
            continue

        # translate strings, functions, names, and comments entirely
        elif (token_type in Token.Literal.String
                or token_type in Token.Name.Function
                or token_type in Token.Comment
                or token_type in Token.Name.Class
                or token_type in Token.Name.Variable
                or token_type in Token.Name.Declaration
                or token_type in Token.Name.Type
                or token_type in Token.Name.Exception
                or token_type in Token.Name
                or token_type in Token.Attribute
        ):
            if len(token_value) == 1:
                translated_content.append(token_value)
                continue
            translated_text = translate(token_value, from_lang, to_lang)
            translated_content.append(translated_text)
        elif token_type in Token.Keyword:
            t = _translate_keyword(token_value, from_lang, to_lang, code_lang, code_version)
            translated_content.append(t)
        else:
            translated_content.append(token_value)
    return ''.join(translated_content)

def _translate_keyword(keyword: str, from_lang: str, to_lang: str, code_lang: str, code_version: str) -> str:
    lookup_table = get_lang_lookup(from_lang, to_lang, code_lang, code_version)
    if keyword in lookup_table:
        return lookup_table[keyword]
    else:
        return keyword

if __name__ == "__main__":
    input_file_path = "../test_in/main.java"  # Change this to your input file path
    output_file_path = "../out/french.java"  # Change this to your desired output file path
    process_code_file(input_file_path, output_file_path, "en", "fr", "Java", "SE 17 LTS", write=False)

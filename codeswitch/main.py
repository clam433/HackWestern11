import re

def translate_token(word, lookup_table, do_truncate=True):
    # Check if the word exists test_in the dictionary
    if word in lookup_table:
        value = lookup_table[word]  # Access the translation directly
        # If the French word is longer, shorten it to match the English word length
        if len(value) > len(word) and do_truncate:
            return value[:len(word)]
        else:
            return value
    return word  # If no match is found, return the original word

def make_sentence(sentence, lang):
    # Define language-specific comment syntax
    language_comments = {
        "javascript": r'//.*|/\*.*?\*/',
        "java": r'//.*|/\*.*?\*/',
        "python": r'#.*',
        "c++": r'//.*|/\*.*?\*/',
        "c": r'//.*|/\*.*?\*/'
    }

    # Get the specific comment regex for the language, default to JavaScript style
    comment_regex = language_comments.get(lang.lower(), r'//.*|/\*.*?\*/')

    # Combine comment regex with other component patterns
    regex = rf'{comment_regex}|\w+|[=+\-*/(),;.]'

    # Find components test_in the sentence
    components = re.findall(regex, sentence)

    return components

if __name__ == "__main__":
    my_comments = ["//", "#", "--", " !", "/* */", " %"]
    table = {
        "let",
        "const",
        "var",
        "function",
        "return",
        "export",
        "extends"
    }
    my_dict = {
        "let": "laisser",
        "const": "constante",
        "var": "variable",
        "function": "fonction"
    }

    # Example usage:
    print(translate_token("let", my_dict, True))  # Output: lai

    # Example usage
    sentence = "let i = 5 + 6 \n /*** This is a Python comment **/"
    language = "java"
    result = make_sentence(sentence, language)
    print(result)

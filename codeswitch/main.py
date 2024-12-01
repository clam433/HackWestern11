import re
my_dict = {
    "let": "laisser",
    "const": "constante",
    "var": "variable",
    "function": "fonction"
}
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


def translateToken(word, table, truncation):
    # Check if the word exists in the dictionary
    if word in table:
        value = table[word]  # Access the translation directly
        # If the French word is longer, shorten it to match the English word length
        if len(value) > len(word) and truncation:
            return value[:len(word)]
        else:
            return value
    return word  # If no match is found, return the original word

# Example usage:
print(translateToken("let", my_dict, True))  # Output: lai

def api(word):
    ...



import re

def makeSentence(sentence, language):
    # Define language-specific comment syntax
    language_comments = {
        "javascript": r'//.*|/\*.*?\*/',
        "java": r'//.*|/\*.*?\*/',
        "python": r'#.*',
        "c++": r'//.*|/\*.*?\*/',
        "c": r'//.*|/\*.*?\*/'
    }
    
    # Get the specific comment regex for the language, default to JavaScript style
    comment_regex = language_comments.get(language.lower(), r'//.*|/\*.*?\*/')
    
    # Combine comment regex with other component patterns
    regex = rf'{comment_regex}|\w+|[=+\-*/(),;.]'
    
    # Find components in the sentence
    components = re.findall(regex, sentence)
    
    return components

# Example usage
sentence = "let i = 5 + 6 \n /*** This is a Python comment **/"
language = "java"
result = makeSentence(sentence, language)
print(result)


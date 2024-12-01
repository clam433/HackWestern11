from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb+srv://christopherl4n:108993mW@codeswitch.5snsl.mongodb.net/?retryWrites=true&w=majority&appName=CodeSwitch")
db = client['CodeSwitch']  # Database name
collection = db['langslookup']  # Collection name
languages = db['languages']  # Languages collection

# Define programming keywords for each language
programming_keywords = {
    "English": ["let", "const", "function", "var", "if", "else", "return", "switch", "case", "try", "catch"],
    "French": ["laisser", "constante", "fonction", "var", "si", "sinon", "retourner", "commutateur", "cas", "essayer", "attraper"]
}

def getTranslationTable(lang, program, dialect, version):
    if program and lang:
        # Find the language document in the 'languages' collection
        language_doc = languages.find_one({"language": lang})
        if not language_doc:
            return f"Language '{lang}' not found in the 'languages' collection."

        # Get the ObjectId of the matching language document
        language_id = language_doc["_id"]

        # Find the English language document
        english_doc = languages.find_one({"language": "English"})
        if not english_doc:
            return "English language not found in the 'languages' collection."

        english_id = english_doc["_id"]

        # Check if the entry already exists in the 'langslookup' collection
        existing_entry = collection.find_one({"language": language_id})
        if existing_entry:
            return "This entry already exists in the database."

        # Create a hashtable of keywords for both languages
        hashtable = {
            "English": programming_keywords.get("English", []),
            lang: programming_keywords.get(lang, [])
        }

        # Prepare the new document for insertion
        language_data = {
            "language": language_id,  # Reference to the language's ObjectId
            "program": program,
            "dialect": dialect,
            "version": version,
            "english": english_id,
            "keywords": hashtable  # Add the hashtable to the document
        }

        # Insert the new document into the 'langslookup' collection
        result = collection.insert_one(language_data)
        return f"Added document with ID {result.inserted_id} to the database."

    else:
        return "Please fill out all required fields."

# Example usage
print(getTranslationTable("French", "Java", "Quebec", "21"))

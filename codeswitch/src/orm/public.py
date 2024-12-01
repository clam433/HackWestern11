from pymongo import MongoClient

client = MongoClient("mongodb+srv://christopherl4n:108993mW@codeswitch.5snsl.mongodb.net/?retryWrites=true&w=majority&appName=CodeSwitch")
db = client['CodeSwitch']  # Database name
collection = db['langs']  # Collection name

def getTranslationTable(lang,program, dialect, version):
    if program and lang:
        if collection.find_one({"language": lang}):
            return lang
        elif collection.find_one({"program" : program}):
            return program
        else:
            language_data = {
                "language" : lang,
                "program" : program,
                "dialect" : dialect,
                "version" : version
            }
        result = collection.insert_one(language_data)
        return f"Added these {result} to the database"
    else:
        return "Please fill out everything"

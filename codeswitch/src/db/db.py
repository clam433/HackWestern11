from mongoengine import connect, Document, StringField, IntField, DictField, ListField, ObjectIdField

connect('CodeSwitch', host='mongodb+srv://christopherl4n:108993mW@codeswitch.5snsl.mongodb.net/?retryWrites=true&w=majority&appName=CodeSwitch')

class Project(Document):
    users = ListField(StringField(), required=True)
    translate_lookup = ListField(ObjectIdField(), requied=True)
    local_keyword_lookup = ListField(ObjectIdField(), required=True)
    author = StringField(required=True)

class TranslateLookup(Document):
    lang_from = StringField(required=True, default="English")
    lang_to = StringField(required=True)
    code_lang = StringField(required=True)
    code_version = StringField(required=True)
    translation_table = DictField(required=True)

    meta = {
        'indexes': [
            'lang_from',
            'code_lang',
            'code_version',
        ]
    }

    def __str__(self):
        return f"{self.lang_from} to {self.lang_to} - {self.code_lang} - {self.code_version} - {self.translation_table}"

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    email = StringField(required=True)
    age = IntField(required=True)

def create_user(username: str, password: str, email: str, age: int):
    user = User(username=username, password=password, email=email, age=age)
    user.save()

def get_user(username: str):
    return User.objects(username=username).first()

def get_all_translate_tables():
    return TranslateLookup.objects()
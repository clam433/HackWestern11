class Test:
    def __init__(self, name, user_list, language):
        self.name = name
        self.user_list = user_list
        self.language = language

    def getProjectName(self):
        return self.name
    
    def getUserList(self):
        return self.user_list
    
    def getLanguage(self):
        return self.language
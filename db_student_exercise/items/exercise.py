class Exercise():
    
    def __init__(self, language, name):
        """
        (language, name)
        """
        self.name = name
        self.language = language

    def __repr__(self):
        return f"{self.name} is an exercise in {self.language}"
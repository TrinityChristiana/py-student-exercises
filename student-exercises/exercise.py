class Exercise():
    def __init__(self, name, language):
        self.name = name
        self.language = language

    def print_details(self):
        print(self.__dict__)

import random

language_list = ["python", "java", "ruby", "javascript", "django"]

def language():
    item = random.choice(language_list)
    del language_list[language_list.index(item)]
    print(item)


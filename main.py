from googletrans import Translator   # need to pip install googletrans==3.1.0a0^C


def open_file(file_name):
    translator = Translator()
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            print(translator.translate(text=line, dest="en").text)


open_file("vietExample.txt")

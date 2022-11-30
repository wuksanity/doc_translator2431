from googletrans import Translator   # need to pip install googletrans==3.1.0a0^C
import threading

#List that holds the resulting documents translated to English
global translatedToEnglish

def open_file(file_name):
    translator = Translator()
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            print(translator.translate(text=line, dest="en").text)

def translatingFunction(threadName):
    translatedToEnglish.append()
    # I think we should translate the files within this threading function

    #Pseudocode:
    # Read each line
    # Translate each line
    # Write each line to a new text document? or string? idk
    # Loop again 
    # Lock (I think the function is acquire())
    # translatedToEnglish.append(the final text dcoument)
    # Unlock (I think it's release())

# She said something about translating multiple documents -- maybe we can use a list of documents ie. documents[0] = vietExample.txt, documents[1] = chineseExample.txt
# and then iterate through each document and pass each document to the threading function?
documents = []

for document in documents:
    thread = threading.Thread(target = translatingFunction, args=document)
    thread.start()

open_file("vietExample.txt")

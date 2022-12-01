from googletrans import Translator   # need to pip install googletrans==3.1.0a0^C
import threading

# List that holds the resulting documents translated to English
global translatedToEnglish
documents = []


def get_user_docs():
    fmt = "file1, file2, ..."
    docs = input(f"Enter the names of each document to translate in the following format: {fmt}")
    documents_array = docs.split(", ")  # probably should validate this...
    return documents_array


def translating_function(file_name):   # just testing if this works so far, can add docs later
    translator = Translator()
    with open(file_name, 'r', encoding='utf8') as file:
        for line in file:
            print(translator.translate(text=line, dest="en").text)
    #translatedToEnglish.append()


def begin_threading(docs):
    for doc in docs:
        thread = threading.Thread(target=translating_function, args=[doc])
        thread.start()


documents = get_user_docs()
print(documents)
begin_threading(documents)

# Pseudocode:
    # Read each line
    # Translate each line
    # Write each line to a new text document? or string? idk
    # Loop again
    # Lock (I think the function is acquire())
    # translatedToEnglish.append(the final text document)
    # Unlock (I think it's release())

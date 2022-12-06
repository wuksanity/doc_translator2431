from googletrans import Translator   # need to pip install googletrans==3.1.0a0^C
import threading

documents = []


def get_user_docs():
    fmt = "file1, file2, ..."
    docs = input(f"Enter the names of each document to translate in the following format: {fmt}")
    documents_array = docs.split(", ")
    return documents_array


def check_user_files(documents):
    documents_updated = documents
    response = "n"
    while response.lower() != "y":  # ensuring user's files are correct
        print()
        for idx, doc in enumerate(documents_updated):
            print(f"{idx + 1}. {doc}")
        print()
        response = input("Do the above files look correct? (Y/N/y/n): ")
        if response.lower() != "y":
            print("Renewing file data...")
            documents_updated = get_user_docs()
        else:
            response = "y"
    return documents_updated


def get_out_file(file_name):
    return file_name[0: file_name.index(".")] + ".output.txt"


def translating_function(files):
    translator = Translator()
    #lock.acquire()
    with open(files[0], 'r', encoding='utf8') as file:
        with open(files[1], 'w') as out:
            for line in file:
                out.write(translator.translate(text=line, dest="en").text + "\n")
    print(files[0] + f" has finished translating, view {files[1]} to see!")
    #lock.release()


def begin_threading(docs):
    #lock = threading.Lock()
    for doc_pair in docs:
        thread = threading.Thread(target=translating_function, args=([doc_pair]))
        thread.start()


documents = get_user_docs()
documents = check_user_files(documents)
documents = list(zip(documents, map(get_out_file, documents)))  # creating tuple: (in_file, out_file)
begin_threading(documents)

# vietExample.txt, mandarinExample.txt

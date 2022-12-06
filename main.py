from googletrans import Translator   # need to pip install googletrans==3.1.0a0^C
import threading

documents = []


def get_user_docs():
    fmt = "file1, file2, ..."
    docs = input(f"Enter the names of each document to translate in the following format: {fmt}")
    documents_array = docs.split(", ")  # probably should validate this...
    return documents_array


def get_out_file(file_name):
    return file_name[0: file_name.index(".")] + ".output.txt"


def translating_function(file_name, lock):
    translator = Translator()
    output_file = get_out_file(file_name)
    lock.acquire()
    with open(file_name, 'r', encoding='utf8') as file:
        with open(output_file, 'w') as out:
            for line in file:
                out.write(translator.translate(text=line, dest="en").text + "\n")

    print()
    print(file_name + f" has finished translating, view {output_file} to see!")
    lock.release()


def begin_threading(docs):
    lock = threading.Lock()
    for doc in docs:
        thread = threading.Thread(target=translating_function, args=(*[doc], lock))
        thread.start()


documents = get_user_docs()
print(documents)
begin_threading(documents)

# vietExample.txt, mandarinExample.txt

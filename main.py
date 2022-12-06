from googletrans import Translator   # need to pip install googletrans==3.1.0a0^C
import threading

documents = []

# Asks the user for input files to translate.
# Parameters: User input for files, with each file being separated by a comma.
# Return value: An array of documents to be translated.
def get_user_docs():
    fmt = "file1, file2, ..."
    docs = input(f"Enter the names of each document to translate in the following format: {fmt}")
    documents_array = docs.split(", ")
    return documents_array

# Asks the user to verify their input documents, if they're incorrect then allows the user to recorrect them.
# Parameters: An array of documents that needs to be verified before being translated.
# Return value: Returns an array of documents that is in the correct form to be translated.
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

# Creates an output text file to be used in a tuple with the input file from the user.
# Parameters: The input file to create an output file that's named similar to the input file.
# Return value: A resulting output file that's named file.output.txt.
def get_out_file(file_name):
    return file_name[0: file_name.index(".")] + ".output.txt"

# Translates each line within a document into English.
# Parameters: A tuple where the first index is the file that needs to be translated, and the second index is an empty out file.
# Return value: A tuple where the first index is the file that needs to be translated, and the second index is the final translated out file.
def translating_function(files):
    translator = Translator()
    with open(files[0], 'r', encoding='utf8') as file:
        with open(files[1], 'w') as out:
            for line in file:
                out.write(translator.translate(text=line, dest="en").text + "\n")
    print(files[0] + f" has finished translating, view {files[1]} to see!")

# Starts the different threads that each translates different documents; incorporates data-level parallelism.
# Parameters: The array of tuples that contain documents that will be translated and their respective output file.
# Return value: No return value, just ensures that the threads begin execution.
def begin_threading(docs):
    lock = threading.Lock()
    for doc_pair in docs:
        thread = threading.Thread(target=translating_function, args=(*[doc_pair], lock))
        thread.start()

documents = get_user_docs()
documents = check_user_files(documents)
documents = list(zip(documents, map(get_out_file, documents)))  # creating tuple: (in_file, out_file)
begin_threading(documents)

# vietExample.txt, mandarinExample.txt

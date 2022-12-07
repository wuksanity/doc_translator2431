from googletrans import Translator   # need to pip install googletrans==3.1.0a0
import threading

# arrays to store default and translated docs
documents = []
translated_docs = []


# Asks the user for input files to translate.
# Parameters: User input for files, with each file being separated by a comma.
# Return value: An array of documents to be translated.
def get_user_docs():
    fmt = "file1, file2, ..."
    docs = input(f"Enter the names of each document to translate in the following format: {fmt}")
    documents_array = docs.split(", ")
    return documents_array


# Asks the user to verify their input documents, if they're incorrect then allows the user to correct them.
# Parameters: An array of documents that needs to be verified before being translated.
# Return value: Returns an array of documents that is in the correct form to be translated.
def check_user_files(docs):
    documents_updated = docs
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
# Parameters: A tuple where the first index is the file that needs to be translated, and the second index is an empty
#             out file.
# Return value: None, outputs translation to a new file
def translating_function(file_name):
    translator = Translator()
    out_file = get_out_file(file_name)
    with open(file_name, 'r', encoding='utf8') as file:
        with open(out_file, 'w') as out:
            for line in file:
                out.write(translator.translate(text=line, dest="en").text + "\n")
    print(file_name + f" has finished translating, view {out_file} to see!")
    # lock here
    translated_docs.append(out_file)
    # unlock here


# Starts the different threads that each translates different documents; incorporates data-level parallelism.
# Parameters: The array of tuples that contain documents that will be translated and their respective output file.
# Return value: No return value, just ensures that the threads begin execution.
def begin_threading(docs):
    for doc in docs:
        thread = threading.Thread(target=translating_function, args=([doc]))
        thread.start()
        thread.join()


def show_out_files(output_files):
    print()
    print("Here are your translated files: ")
    for idx, doc in enumerate(output_files):
        print(f"{idx + 1}. {doc}")


documents = get_user_docs()
documents = check_user_files(documents)
begin_threading(documents)
show_out_files(translated_docs)

# vietExample.txt, mandarinExample.txt

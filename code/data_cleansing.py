import os
import pickle
import glob
import re
import random

#function to read a book and smart split 
def read_book(file_path):
    with open(file_path, encoding='latin-1') as f:
        content = f.readlines()
    content = "".join(content)
    content  = re.split(r'\n\n|\.|\? |! ',content)
    content = [x.replace("\n", " ").strip() for x in content]
    return content

#for simplicity at this time we'll only keep the dialogues starting with the name of the 
#character with all capitalized words and ":". We'll develop more features im future
def filter_data(book): 
    regex = re.compile("^[A-Z ]+:.*$")
    dialogue = [x for x in book if bool(regex.search(x))]
    return dialogue
 
#clean a string of the book after filtering
def clean_string(speech):
    #remove the name of the speaker
    speech = re.sub("^[A-Z ]+: ", "", speech)
    #remove ;, because I don't think that anyone use this nowadays
    speech = re.sub(";", ",", speech)
    return speech


def read_clean_save_data():
    books_path = "raw_data/books/"
    save_path = "tidy_data/books/"
    books_list = glob.glob(books_path  + "*.txt")   
    for path in books_list:
        book = read_book(path)
        book = filter_data(book)
        #we may not able to extract a dialogue at this time
        if len(book) > 1:
            print(random.choice(book))
            book = [clean_string(x) for x in book]
            save_path2 = re.sub(books_path, "", path)
            save_path2 = re.sub("txt", "pickle", save_path2)
            save_path2 = save_path + save_path2
            with open(save_path2, 'wb') as f:
                pickle.dump(book, f)

            
if __name__ == "__main__" :
    read_clean_save_data()


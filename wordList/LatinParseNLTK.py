import pandas as pd;

import nltk
nltk.download('punkt')
nltk.download('words')
from nltk.corpus import words
nltk.download('Latin')

file_path = 'Cholti_WordList_Appended.xlsx'
sheet_name = "Sheet1"
column_to_read = "Standardized Ch'olti"
column_to_write = "Clean Latin" 


df = pd.read_excel(file_path, sheet_name=sheet_name)
latin_words = set(nltk.corpus.words.words('latin'))


# Function to check if a word is Latin
def is_latin(word):
    return word.lower() in latin_words

def process_words(column_to_read,column_to_write):

    latin_words_if_any = []
    if column_to_read or column_to_write not in df.columns:
        print("One of the columns is not in the sheet")
    
    for index, row in df.iterrows():
        value = row[column_to_read]
        if str(value).__contains__(";"):
            value = str(value).replace(";","")
            
        words = str(value).split()
        for word in words:
            if is_latin(word):
                latin_words_if_any.append(word)
            else:
                print("not a latin word")


def main():
    process_words(column_to_read,column_to_write)
if __name__ == "__main__":
    main()
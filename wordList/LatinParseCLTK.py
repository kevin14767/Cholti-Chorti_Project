#script to parse through words and check if they're latin
import pandas as pd;
from cltk.languages.utils import get_lang
from cltk.languages.glottolog import LANGUAGES
from cltk.core.exceptions import UnknownLanguageError
import torch



file_path = 'Cholti_WordList_Appended.xlsx'
sheet_name = "Sheet1"
column_to_read = "Standardized Ch'olti"
column_to_write = "Clean Latin" 

df = pd.read_excel(file_path, sheet_name=sheet_name)

def is_latin(word):
    try:
        lang = 'lat'
        return lang == 'lat'
        #return lang in LANGUAGES and LANGUAGES[lang]['latitude_name'] == 'Latin'
    except UnknownLanguageError as e:
        print(f"Error: {e}")
        return False

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
    print(latin_words_if_any)            

def main():
    process_words(column_to_read,column_to_write)
if __name__ == "__main__":
    main()
#python script first thing i want to do is read excel column and check if its spanish 
#if so write to new column.

import pandas as pd
from langdetect import detect

def is_spanish(word):
    try:
        # Attempt to detect the language of the word
        language = detect(word)

        # Check if the detected language is Spanish
        return language == 'es'
    except:
        # Handle cases where language detection fails
        return False

def process_excel(file_path, input_column, output_column, third_column):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Check if the specified column exists in the DataFrame
    if input_column not in df.columns:
        print(f"Column '{input_column}' not found in the Excel file.")
        return
    # Check if the specified column exists in the DataFrame
    if output_column not in df.columns:
        print(f"Column '{output_column}' not found in the Excel file.")
        return
    # Iterate over the rows in the DataFrame
    for index, row in df.iterrows():
        # Get the value from the specified input column
        value = row[input_column]

        # Split the text into wordsx
        words = str(value).split(";")
        #Detect the language for each word and check if it's Spanish
        spanish_words = []
        clean_cholti = []
        for word in words:
            word = word.strip()
            if is_spanish(word):
                spanish_words.append(word)
            #here the word isn't spanish just put it into cholti so we can figure out if its latin or not or ?
            else:
                clean_cholti.append(word)

        spanish_text = ", ".join(spanish_words)
        clean_cholti_text = ", ".join(clean_cholti)
        # Write the Spanish text to the specified output column in the same row
        df.at[index, output_column] = spanish_text
        df.at[index, third_column] = clean_cholti_text
    

    # Write the updated DataFrame to the output Excel file
    df.to_excel(file_path, index=False)
    


def main():
    process_excel('Cholti_WordList.xlsx',"Standardized Ch'olti", "Clean Spanish", "Clean Cholti")
if __name__ == "__main__":
    main()

        
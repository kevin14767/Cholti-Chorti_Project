import pandas as pd

input = 'Flowing_translation_spanish.txt'
file_path = 'Liturgy&OriginalTranscription.xlsx'
column_to_write = 'Appendix Spanish Flowing'
sheet_name = "Sheet1"
df = pd.read_excel(file_path)

with open(input, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        line = line.strip()
        df.at[i, column_to_write] = line
        i += 1

    df.to_excel(file_path, sheet_name=sheet_name, index=False)


        
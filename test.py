import pandas as pd
from openpyxl import load_workbook

# Define the path to your Excel file
excel_file = r'C:\Users\Kevin\Downloads\Cholti_Project\CholtiProject\Cholti-Chorti_Project\Cholti_TranscriptionScheme-Regularized_Spelling.xlsx'

# Load the Excel file into a DataFrame
df = pd.read_excel(excel_file, sheet_name='Sheet1')

# Define the specified column and the column to write to
specified_column = 'Cholti'
column_to_write = 'Transcription Scheme'

# Iterate through the DataFrame
for index, row in df.iterrows():
    value = row[specified_column]
    if not pd.isna(value):
        # Iterate through the Cholti word
        newWord = ""
        for i in range(len(value)):
            first = value[i]
            if i < len(value) - 1:
                second = value[i + 1]
                if first == 'c' and (second == 'i' or second == 'e'):
                    newWord += 's'
                else:
                    newWord += first
            else:
                newWord += first
        # Update the 'Transcription Scheme' column with the new value
        df.at[index, column_to_write] = newWord

# Create a Pandas ExcelWriter to write the updated DataFrame to the Excel file
with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
    writer.book = load_workbook(excel_file)
    writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
    df.to_excel(writer, sheet_name='Sheet1', index=False)

print("Data written to the Excel file.")

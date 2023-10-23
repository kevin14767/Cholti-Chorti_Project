#libaries
import pandas as pd
from openpyxl import load_workbook
#reading from the excel sheet
excel_file = r'"C:\Users\Kevin\Downloads\Cholti_Project\CholtiProject\Cholti-Chorti_Project\Cholti_WordList8Jan2009.xls"'
sheet_name = 'Sheet1';
#dataframe
df = pd.read_excel(excel_file, sheet_name=sheet_name);
#skips the first row
start_row = 1;
#column to write too
specified_column = 'Cholti';
column = 'Transcription'
#iterating through Cholti column
print(df.columns)

for index, row in df.iterrows():
    value = row[specified_column];
    if not pd.isna(value):
    #if(value != None):
    #iterate through the cholti word
        for i in range(len(value)-1):
            first = value[i];
            second = value[i+1];
            if(first == 'c'):
                if(second == 'i' or second == 'e'):
                    #data to write
                    newWord = value.replace('c','s');
                    df.at[row - 1, column] = newWord
                    #cell = f"{specified_column}{row}"
                    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                        writer.book = load_workbook(excel_file)
                        writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
                    #sheet[cell] = newWord
                    df.to_excel(writer,sheet_name='Sheet1', index=False);




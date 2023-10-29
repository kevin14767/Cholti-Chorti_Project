#feed lines from the original transcription to the v1 of excel sheet
#tasks are to add the entries of the page and reset at each page, add this transcription of it as well in a new column that's all so far.
import openpyxl

workbook = openpyxl.load_workbook("FirstVersion.xlsx")
sheet = workbook['Sheet1']
with open('OriginalTranscriptEdited.txt', 'r') as text_file:
    text_data = text_file.readlines()

column = 'D'
row_number = 2
val = False;
entryNum = 0
pageNum = 0
for line in text_data:
    char = line[0]
    if char == 'P' or char == 'R' or char == '{':
        row_number += 1
        entryNum += 1;
    if line.strip() == 'Â¬':
        val = False
        entryNum = 0
    if val:
        value = str(pageNum) + "." + str(entryNum)
        cell = sheet[column + str(row_number)]
        cell.value = value        
    if line.strip().isdigit():
        val = True
        pageNum = int(line)
    
        


    
    
    
workbook.save('FirstVersion.xlsx')

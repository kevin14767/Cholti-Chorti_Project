#adding a new column with the orignal transcription from the "OriginalTranscriptionEdited.txt" file 
import openpyxl
workbook = openpyxl.load_workbook("SecondVersion.xlsx")
sheet = workbook['Sheet1']

with open('OriginalTranscriptEdited.txt', 'r') as text_file:
    text_data = text_file.readlines()

column = 'F'
starting_row = 1;
row_number = 2;
for line in text_data:
    char = line[0];
    #this line of code runs into problems when there's multiple entries in numerous lines
    if char == 'P' or char == 'R' or char == 'ï»¿':
        value = str(line)
        value = value[2:].replace("_","")
        value = value.strip();
        cell = sheet[column + str(row_number)]
        cell.value = value
        row_number += 1

workbook.save("ThirdVersion.xlsx")

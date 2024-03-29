#this python script is intended to convert "The Religious Sections" of the Moran Manuscript into a database file
#Excel sheet format will be a answer and response format, naturally the manuscript follows these format as well

#Formatting:
#Line Number 1-530
#Manuscript entry Page.59 to 80
#Line entry in the actual manuscript page. i.e entry number 1 entry number 2 however sometimes they are in the same line entry or in
#multiple lines for one entry. 
#4 columns: standardized version of the original ch'olti, morphemic gloss, a literal english translation, a flowing english translation

#old version disregard, although this beta is later used in txtFiletoExcel.py

import pandas as pd

input = 'liturgy30June06.txt'
output = 'copyy.xlsx'

df = pd.DataFrame(columns=['Pregunta/Respuesta','Line Number', 'Manuscript Page','Entry in Page','Standardized Cholti','Morphemic Gloss',
                           'Literal English Translation','Flowing English Translation'])

switch = 'P';
newEntry = False;

with open(input, 'r') as file:
    for line in file:
        line = line.strip()
        line_number = None
        data_to_append = {}
        if line.isdigit():
            #if we know its a digit we know that the next 4 lines are in order of the columns
            line_number = int(line)
            data_to_append[1] = {'Line Number': line_number}

        data_to_append[0] = {'Pregunta/Respuesta':switch}
        print(data_to_append)
        df = df._append(data_to_append,ignore_index=True)
        if (switch == 'P'):
            switch = 'F'
        else:
            switch = 'P'
        


df.to_excel(output, index=False)
        

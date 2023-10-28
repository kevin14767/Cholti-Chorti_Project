#this python script is intended to convert "The Religious Sections" of the Moran Manuscript into a database file
#Excel sheet format will be a answer and response format, naturally the manuscript follows these format as well

#Formatting:
#Line Number 1-530
#Manuscript entry Page.59 to 80
#Line entry in the actual manuscript page. i.e entry number 1 entry number 2 however sometimes they are in the same line entry or in
#multiple lines for one entry. 
#4 columns: standardized version of the original ch'olti, morphemic gloss, a literal english translation, a flowing english translation

import pandas as pd

input = 'liturgy30June06edited.txt'
output = 'copyy.xlsx'

df = pd.DataFrame(columns=['Pregunta/Respuesta','Line Number', 'Manuscript Page','Entry in Page','Standardized Cholti','Morphemic Gloss',
                           'Literal English Translation','Flowing English Translation'])

switch = 'P';
newEntry = False;

with open(input, 'r') as file:
    lines = file.readlines()
    chunk_size = 5
    data_to_append = {}
    for i in range(0, len(lines), chunk_size):
        chunk = [line.strip() for line in lines[i:i + chunk_size]]
        print(chunk[0])
        data_to_append = {'Pregunta/Respuesta': switch, 'Line Number': chunk[0],'Standardized Cholti': chunk[1], 'Morphemic Gloss':chunk[2]
                          ,'Literal English Translation': chunk[3], 'Flowing English Translation':chunk[4] }
        if (switch == 'P'):
            switch = 'R'
        else:
            switch = 'P'
        #df = df._append(data_to_append, ignore_index= True)
    
        
#df.to_excel(output, index=False)


        
        
#python script just removed any empty lines in the Original Transcription.txt file to make the extraction of data easier for the txtFileToExcel.py script
#writes output to OriginalTranscriptEdited.txt

import pandas as pd

input = 'Original Transcription.txt'

with open(input, 'r') as file:
    lines = file.readlines()

with open('OriginalTranscriptEdited.txt', 'w') as file:
    for line in lines:
        if line.strip():
            file.write(line)

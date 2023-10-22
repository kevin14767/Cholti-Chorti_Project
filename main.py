import pandas as pd
#reading from the excel sheet
excel_file = r'C:\Users\Kevin\Downloads\Cholti_Project\CholtiProject\Cholti-Chorti_Project\Cholti_WordList8Jan2009.xls'
sheet_name = 'Sheet1';
df = pd.read_excel(excel_file, sheet_name=sheet_name);
#list of strings to consider adding
my_list_to_add= [];
start_row = 19
#for value in column C starting from row 21
for value in df['Unnamed: 2'].iloc[start_row:]:
    str_value = str(value);
    print(str_value);
    #iterating through the ch'olti word
    for i in range(len(str_value)- 1):
        first_value = str_value[i];
        second_value = str_value[i+1];
        
        if (first_value == 'c'):
            if(second_value != 'h'):
                my_list_to_add.append(str_value);


s_wordlist = [];
k_wordlist = [];

#ignored all words with ch in them, only focusing on words with other letters following c
for value in my_list_to_add:
    #statements for if followed by i,e write s 
    for i in range(len(value)- 1):
        one = value[i];
        two = value[i];
        if (one == 'c'):
            if(two == 'i' or two == 'e'):
                s_wordlist.append(value)
            elif (two == 'a' or two == 'o' or two == 'u'):
             #statement for if followed by a,o,u write k
                k_wordlist.append(value)



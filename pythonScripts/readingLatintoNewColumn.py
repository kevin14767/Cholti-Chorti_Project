import pandas as pd

# Read the Excel file
file_path = "Cholti_WordList.xlsx"
sheet_name = "Sheet1"  # Replace with your sheet name
column_to_read = "Clean Cholti"  # Replace with the column you want to read
column_to_write = "Clean Latin"  # Replace with the column where you want to write

# Read the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

partial_string = "idem"
# Access the specific column and iterate through its values
for index, row in df.iterrows():
    # Get the value from the specified input column
    value = row[column_to_read]
    # Perform any processing on the value if needed
    words = str(value).split()
    words_to_keep = []
    word_to_write = []
    for word in words:
        if partial_string in word:
            df.at[index, column_to_write] = word
        else:
            words_to_keep.append(word)
    
    words_kept = " ".join(words_to_keep)
    df.at[index, column_to_read] = words_kept


# Save the modified DataFrame back to the Excel file
df.to_excel(file_path, sheet_name=sheet_name, index=False)

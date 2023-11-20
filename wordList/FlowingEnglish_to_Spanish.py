from googletrans import Translator
import pandas as pd

# Load the Excel file into a DataFrame
excel_file_path = 'Liturgy&OriginalTranscription.xlsx'
df = pd.read_excel(excel_file_path)
# Create a translator object
translator = Translator()
def translate_text(text):
    try:
        translated_text = translator.translate(text, dest='es').text
        return translated_text
    except Exception as e:
        print(f"Translation error: {e}")
        return None

# Translate the values in column 'A' and create a new column 'B' with the translations

df['Flowing Spanish Translation'] = [translate_text(text) for text in df['Flowing English Translation']]

# Save the updated DataFrame to a new Excel file or overwrite the existing one
output_excel_path = 'Liturgy&OriginalTranscription.xlsx'
df.to_excel(output_excel_path, index=False)

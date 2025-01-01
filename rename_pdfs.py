import os
import re
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    text = []
    try:
        with fitz.open(pdf_path) as pdf:
            for page in pdf:
                text += page.get_text('words')
                page_words = [word[4] for word in text]
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    #print(page_words)
    return page_words

def find_date_and_invoice(words):
    """Find date and invoice number in the extracted text."""

    invoice_number = None  # Default value if target_word is not found
    for i, word in enumerate(words):
        if word == 'Factuurnummer' or word == 'Factuurnr:':
            #print('entered if number')
            # Ensure we're not at the last word to avoid IndexError
            if i + 1 < len(words):
                number_pattern = r'(^\d+$)'
                if re.match(number_pattern, words[i + 1]):
                    #print('entered i + 1 number')
                    invoice_number = words[i + 1]
                elif re.match(number_pattern, words[i + 2]):
                    #print('entered i + 2 number')
                    invoice_number = words[i + 2]
        if word == 'Factuurdatum' or word == 'Datum:':
            #print('entered if date')
            # Ensure we're not at the last word to avoid IndexError
            if i + 1 < len(words):
                date_pattern = r'(\d{2})[-.](\d{2})[-.](\d{4})'
                if re.match(date_pattern, words[i + 1]):
                    #print('entered i + 1 date')
                    date = words[i + 1]
                elif re.match(date_pattern, words[i + 2]):
                    #print('entered i + 2 date')
                    date = words[i + 2]
                    #print(date)

    formatted_date = convert_date_format(date)
    return formatted_date, invoice_number

def convert_date_format(date_string):
    """
    Converts a date from DD-MM-YYYY or DD.MM.YYYY to YYYYMMDD format.
    
    Args:
        date_string (str): Input date string.
    
    Returns:
        str: Date in YYYYMMDD format, or None if the input doesn't match.
    """
    # Regex to match DD-MM-YYYY or DD.MM.YYYY
    date_pattern = r'(\d{2})[-.](\d{2})[-.](\d{4})'
    match = re.match(date_pattern, date_string)
    
    if match:
        day, month, year = match.groups()
        year = year[2:]
        return f"{year}{month}{day}"  # Rearrange to YYYYMMDD
    else:
        return None  # Return None if input doesn't match the pattern

def rename_pdf_files(folder_path):
    """Rename PDF files based on extracted date and invoice number."""
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith('.pdf'):
            full_path = os.path.join(folder_path, file_name)
            print(f"Processing: {file_name}")
            
            # Extract text
            words = extract_text_from_pdf(full_path)
            
            # Find date and invoice number
            date, invoice_number = find_date_and_invoice(words)
            
            if date and invoice_number:
                # Build the new file name
                new_name = f"{date} factuur {invoice_number}.pdf"
                new_path = os.path.join(folder_path, new_name)
                
                # Rename the file
                try:
                    os.rename(full_path, new_path)
                    print(f"Renamed to: {new_name}")
                except Exception as e:
                    print(f"Error renaming {file_name}: {e}")
            else:
                print(f"Could not find date and invoice number in {file_name}")

if __name__ == "__main__":
    folder_path = input("Enter the folder path containing PDF files: ")
    if os.path.isdir(folder_path):
        rename_pdf_files(folder_path)
    else:
        print("Invalid folder path.")

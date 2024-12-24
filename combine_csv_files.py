import pandas as pd
import time
import os
import csv

# Load the provided CSV files to inspect their content
total_file_path = 'total.csv'
a1_file_path = 'a1.csv'
a2_file_path = 'a2.csv'
b_file_path = 'b.csv'

# Read the CSV file and filter out the unwanted row
with open('total.csv', 'r', encoding='utf-8') as infile, open('total_out.csv', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)
    
    for row in reader:
        # Check if the row matches the unwanted row
        if row != ["", "", "", "", "", "", "", "", "", "ΟΧΙ"]:
            writer.writerow(row)
        else:
            print("Row removed: ", row)

cleared_total = 'total_out.csv'   
# Read again total file without row with empty values in column "Όνομα"
total_file_data = pd.read_csv(cleared_total)
# Parse a1, a2, b files as it uses a semi-colon delimiter
a1_file_data = pd.read_csv(a1_file_path, sep=';', engine='python')
a2_file_data = pd.read_csv(a2_file_path, sep=';', engine='python')
b_file_data = pd.read_csv(b_file_path, sep=';', engine='python')
# Display the first few rows of each file to understand their structure

# Convert the dates to a consistent format
# Remove rows with empty values in column "ΗΜΕΡΟΜΗΝΙΑ ΑΞΙΟΛΟΓΗΣΗΣ Α1/Α"

total_file_data = total_file_data[total_file_data["ΑΦΜ"].astype(str).str.len() == 9]
print(total_file_data)

total_file_data["ΗΜΕΡΟΜΗΝΙΑ ΑΞΙΟΛΟΓΗΣΗΣ Α1/Α"] = pd.to_datetime(total_file_data["ΗΜΕΡΟΜΗΝΙΑ ΑΞΙΟΛΟΓΗΣΗΣ Α1/Α"], format="%d/%m/%Y %H:%M", errors="coerce")
a1_file_data = a1_file_data.dropna(subset=["Ημερομηνία-Αξιολόγησης"])
a1_file_data["Ημερομηνία-Αξιολόγησης"] = a1_file_data["Ημερομηνία-Αξιολόγησης"].str[:-8]
a1_file_data["Ημερομηνία-Αξιολόγησης"] = pd.to_datetime(a1_file_data["Ημερομηνία-Αξιολόγησης"], format="%d/%m/%Y %H:%M", errors="coerce")

# print(total_file_data)
# print(a1_file_data)
# print(a2_file_data.head())
# print(b_file_data.head())

# Merge the DataFrames
merged_df = pd.merge(
    total_file_data,
    a1_file_data,
    left_on=["ΗΜΕΡΟΜΗΝΙΑ ΑΞΙΟΛΟΓΗΣΗΣ Α1/Α", "ΑΦΜ"],
    right_on=["Ημερομηνία-Αξιολόγησης", "Αξιολογούμενος-ΑΦΜ"],
    how="left"
)
merged_df.to_csv("merged_data.csv", index=False)

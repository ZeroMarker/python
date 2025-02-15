import csv
import json

def convert_to_array(value):
    # Split by commas if there are multiple values, else keep it as a single value
    return [item.strip() for item in value.split(',')] if ',' in value else value.strip()

csv_file = 'data.csv'
json_file = 'data.json'

# Read CSV
with open(csv_file, mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = []
    
    for row in reader:
        for key, value in row.items():
            row[key] = convert_to_array(value)
        rows.append(row)

# Write JSON
with open(json_file, mode='w', encoding='utf-8') as f:
    json.dump(rows, f, indent=4, ensure_ascii=False)

print("CSV has been converted to JSON successfully!")

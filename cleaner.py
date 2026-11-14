import csv
from pathlib import Path

input_file = Path("input.csv")
output_file = Path("cleaned.csv")

with input_file.open("r", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    if not headers:
        raise ValueError("The CSV file needs a header row.")

    cleaned_rows = []
    seen_rows = set()

    for row in reader:
        cleaned_row = {
            header: (row.get(header) or "").strip()
            for header in headers
        }

        # Skip rows where every cell is blank.
        if not any(cleaned_row.values()):
            continue

        # Skip rows that are exact duplicates.
        row_key = tuple(cleaned_row[header] for header in headers)
        if row_key in seen_rows:
            continue

        seen_rows.add(row_key)
        cleaned_rows.append(cleaned_row)

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(cleaned_rows)

print(f"Done! Saved {len(cleaned_rows)} rows to {output_file}.")
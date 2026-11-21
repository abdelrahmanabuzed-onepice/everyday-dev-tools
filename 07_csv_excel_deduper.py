"""
Tool 7: Fast CSV & Lead Deduplicator & Cleaner
Trims whitespace, fixes broken encodings, removes duplicate rows, and reports clean yield.
Author: Abdelrahman Abouzed
"""

import sys
import os
import csv


def clean_csv(input_path: str, output_path: str = None, key_column: str = None):
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        return

    if not output_path:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_deduped{ext}"

    seen_keys = set()
    cleaned_rows = []
    total_rows = 0
    duplicate_rows = 0

    # Auto-detect encoding
    encodings_to_try = ["utf-8-sig", "utf-8", "windows-1256", "latin1"]
    content = None
    used_encoding = "utf-8"

    for enc in encodings_to_try:
        try:
            with open(input_path, "r", encoding=enc) as f:
                content = f.read()
                used_encoding = enc
                break
        except Exception:
            continue

    if content is None:
        print("[!] Could not decode file with standard encodings.")
        return

    lines = content.splitlines()
    reader = csv.reader(lines)
    header = next(reader, None)

    if not header:
        print("[!] Empty CSV file.")
        return

    key_idx = 0
    if key_column and key_column in header:
        key_idx = header.index(key_column)

    cleaned_rows.append(header)

    for row in reader:
        if not row or not any(row):
            continue
        total_rows += 1
        
        # Identifier for deduplication
        identifier = row[key_idx].strip().lower() if key_idx < len(row) else tuple(row)
        if identifier in seen_keys:
            duplicate_rows += 1
            continue
            
        seen_keys.add(identifier)
        cleaned_rows.append([cell.strip() for cell in row])

    # Write cleaned CSV
    with open(output_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(cleaned_rows)

    print("\n" + "=" * 55)
    print("      CSV DEDUPLICATOR & CLEANER REPORT")
    print("=" * 55)
    print(f"Source File:       {input_path} ({used_encoding})")
    print(f"Total Rows Scanned: {total_rows}")
    print(f"Duplicates Removed: {duplicate_rows}")
    print(f"Clean Rows Kept:   {len(cleaned_rows) - 1}")
    print(f"Cleaned Output:    {output_path}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python 07_csv_excel_deduper.py <input.csv> [output.csv] [key_column_name]")
        sys.exit(0)
    in_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    col = sys.argv[3] if len(sys.argv) > 3 else None
    clean_csv(in_file, out_file, col)

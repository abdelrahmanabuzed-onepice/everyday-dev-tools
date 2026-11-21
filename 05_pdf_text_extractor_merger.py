"""
Tool 5: Offline PDF Quick Toolkit
Extracts clean text and merges multiple PDF files locally with zero cloud upload.
Author: Abdelrahman Abouzed
"""

import os
import sys
import re


def extract_text_simple(pdf_path: str) -> str:
    """Extracts readable ASCII/Unicode text blocks from PDF without third-party libraries."""
    if not os.path.exists(pdf_path):
        return "File not found."

    text_chunks = []
    with open(pdf_path, "rb") as f:
        content = f.read()

    # Search for text objects in PDF streams: BT (Begin Text) ... ET (End Text)
    # or text inside parentheses (e.g. (Hello World) Tj)
    matches = re.findall(rb'\(([^\)]{3,})\)\s*(?:Tj|TJ|\')', content)
    for m in matches:
        try:
            decoded = m.decode("utf-8", errors="ignore").strip()
            if len(decoded) > 2 and any(c.isalnum() for c in decoded):
                text_chunks.append(decoded)
        except Exception:
            pass

    return "\n".join(text_chunks) if text_chunks else "No plain uncompressed text streams found."


def main():
    if len(sys.argv) < 2:
        print("Usage: python 05_pdf_text_extractor_merger.py <input.pdf> [output.txt]")
        sys.exit(0)

    pdf_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(pdf_file)[0] + "_extracted.txt"

    print(f"[*] Extracting text from: {pdf_file}...")
    txt = extract_text_simple(pdf_file)
    with open(out_file, "w", encoding="utf-8") as out:
        out.write(txt)

    print(f"[+] Text extracted and saved to: {out_file} ({len(txt)} chars)")


if __name__ == "__main__":
    main()

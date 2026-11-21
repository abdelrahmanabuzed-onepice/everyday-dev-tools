"""
Tool 3: Smart Desktop & Downloads Sorter
Automatically sorts messy folders into clean, organized subfolders by file category.
Author: Abdelrahman Abouzed
"""

import os
import shutil
import sys

CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".txt", ".csv", ".rtf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
    "Installers": [".exe", ".msi", ".bat", ".cmd"],
    "Code_Scripts": [".py", ".js", ".html", ".css", ".json", ".sql", ".ps1", ".cpp", ".java"],
    "Media_Audio_Video": [".mp4", ".mkv", ".mp3", ".wav", ".avi", ".mov"]
}


def organize_folder(folder_path: str, dry_run: bool = False):
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        return

    print(f"\n[*] Scanning & Sorting: {folder_path} (Dry Run: {dry_run})")
    moved_count = 0

    for item in os.listdir(folder_path):
        src_path = os.path.join(folder_path, item)
        if os.path.isdir(src_path):
            continue  # Don't move already created subfolders

        ext = os.path.splitext(item)[1].lower()
        if not ext:
            continue

        target_category = "Other_Files"
        for cat_name, extensions in CATEGORIES.items():
            if ext in extensions:
                target_category = cat_name
                break

        dest_dir = os.path.join(folder_path, target_category)
        dest_path = os.path.join(dest_dir, item)

        if not dry_run:
            os.makedirs(dest_dir, exist_ok=True)
            # Avoid overwriting
            if os.path.exists(dest_path):
                base, ext_part = os.path.splitext(item)
                dest_path = os.path.join(dest_dir, f"{base}_copy{ext_part}")
            shutil.move(src_path, dest_path)
            
        print(f"  -> [{target_category}] {item}")
        moved_count += 1

    print(f"\n[+] Total items sorted: {moved_count}\n")


if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    organize_folder(target_dir, dry_run=False)

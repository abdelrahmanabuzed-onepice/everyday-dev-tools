"""
Tool 10: Differential Smart File Backup with SHA-256 Verification
Only backs up new or modified files, verifying file hashes to prevent data corruption.
Author: Abdelrahman Abouzed
"""

import os
import shutil
import hashlib
import sys


def get_file_hash(filepath: str) -> str:
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(65536):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return ""


def run_backup(source_dir: str, backup_dir: str):
    if not os.path.isdir(source_dir):
        print(f"Source directory not found: {source_dir}")
        return

    os.makedirs(backup_dir, exist_ok=True)
    print("\n" + "=" * 55)
    print("      DIFFERENTIAL FILE BACKUP (SHA-256 VERIFIED)")
    print("=" * 55)
    print(f"Source: {source_dir}")
    print(f"Dest:   {backup_dir}\n")

    copied_count = 0
    skipped_count = 0

    for root, _, files in os.walk(source_dir):
        rel_path = os.path.relpath(root, source_dir)
        target_root = os.path.join(backup_dir, rel_path)
        os.makedirs(target_root, exist_ok=True)

        for f in files:
            src_file = os.path.join(root, f)
            dst_file = os.path.join(target_root, f)

            needs_copy = False
            if not os.path.exists(dst_file):
                needs_copy = True
            else:
                # Compare mod time and hash if size differs
                if os.path.getsize(src_file) != os.path.getsize(dst_file) or get_file_hash(src_file) != get_file_hash(dst_file):
                    needs_copy = True

            if needs_copy:
                shutil.copy2(src_file, dst_file)
                print(f"  [+] Copied/Updated: {f}")
                copied_count += 1
            else:
                skipped_count += 1

    print("-" * 55)
    print(f"[+] Backup Complete: {copied_count} files backed up, {skipped_count} unchanged files skipped.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python 10_smart_file_backup.py <source_folder> <backup_folder>")
        sys.exit(0)
    run_backup(sys.argv[1], sys.argv[2])

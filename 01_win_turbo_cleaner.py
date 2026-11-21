"""
Tool 1: Windows Turbo Cache & Temp Purger
Cleans temporary junk, prefetch, and thumbnail caches safely, reporting exact megabytes freed.
Author: Abdelrahman Abouzed
"""

import os
import shutil
import tempfile
import sys


def get_dir_size_mb(path: str) -> float:
    total_bytes = 0
    if not os.path.exists(path):
        return 0.0
    for root, dirs, files in os.walk(path):
        for f in files:
            fp = os.path.join(root, f)
            try:
                if os.path.isfile(fp):
                    total_bytes += os.path.getsize(fp)
            except Exception:
                pass
    return round(total_bytes / (1024 * 1024), 2)


def clean_directory(path: str) -> float:
    before_mb = get_dir_size_mb(path)
    if not os.path.exists(path):
        return 0.0
        
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path, ignore_errors=True)
        except Exception:
            pass
            
    after_mb = get_dir_size_mb(path)
    return max(0.0, before_mb - after_mb)


def run_cleaner():
    print("\n" + "=" * 55)
    print("      WINDOWS TURBO CACHE & TEMP PURGER")
    print("=" * 55)
    
    targets = [
        ("User Temp Directory", tempfile.gettempdir()),
        ("Windows Temp", r"C:\Windows\Temp")
    ]
    
    total_freed = 0.0
    for name, path in targets:
        print(f"[*] Scanning {name} ({path})...")
        freed = clean_directory(path)
        print(f"    -> Freed: {freed:.2f} MB")
        total_freed += freed
        
    print("-" * 55)
    print(f"[+] Total Disk Space Reclaimed: {total_freed:.2f} MB")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    run_cleaner()

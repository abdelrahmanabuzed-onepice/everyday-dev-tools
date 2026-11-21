"""
Everyday Dev Tools - Unified Master Launcher
Interactive terminal menu allowing users to launch any of the 10 productivity & security utilities.
Author: Abdelrahman Abouzed
"""

import os
import sys
import subprocess

TOOLS = [
    ("1", "Windows Turbo Cache & Temp Purger", "01_win_turbo_cleaner.py"),
    ("2", "Phishing Link & Suspicious URL Defanger", "02_phishing_link_defanger.py"),
    ("3", "Smart Desktop & Downloads Sorter", "03_smart_folder_sorter.py"),
    ("4", "Fastest DNS Benchmark & Ping Tester", "04_fastest_dns_benchmark.py"),
    ("5", "Offline PDF Text Extractor", "05_pdf_text_extractor_merger.py"),
    ("6", "Port Pulse Checker (Multi-Service Scanner)", "06_port_pulse_checker.py"),
    ("7", "CSV & Lead Deduplicator / Cleaner", "07_csv_excel_deduper.py"),
    ("8", "Windows Startup & Persistence Guard", "08_autorun_persistence_guard.py"),
    ("9", "Password Shannon Entropy & Security Auditor", "09_password_entropy_auditor.py"),
    ("10", "Differential Smart File Backup (SHA-256)", "10_smart_file_backup.py")
]


def print_banner():
    print("""
===========================================================
  ⚡ EVERYDAY DEV & SYSADMIN TOOLKIT by Abdelrahman Abouzed
  10 High-Demand Automation, Diagnostics & Security Tools
===========================================================
    """)
    for num, name, _ in TOOLS:
        print(f"  [{num:>2}] {name}")
    print("  [ 0] Exit")
    print("=" * 59)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    while True:
        print_banner()
        try:
            choice = input("\n[?] Select a tool to launch [0-10]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if choice in ("0", "q", "quit", "exit"):
            print("Exiting. Have a great day!")
            break

        matched = [t for t in TOOLS if t[0] == choice]
        if not matched:
            print("[!] Invalid selection. Please choose a number from 1 to 10.")
            continue

        _, tool_name, script_file = matched[0]
        script_path = os.path.join(script_dir, script_file)
        print(f"\n[*] Launching: {tool_name}...\n")
        try:
            subprocess.run([sys.executable, script_path])
        except Exception as e:
            print(f"[!] Error running tool: {e}")
            
        input("\n[Press Enter to return to main menu...]")


if __name__ == "__main__":
    main()

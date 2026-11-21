# Everyday Dev & SysAdmin Toolkit ⚡🛠️
### 10 Practical, Zero-Dependency Python Utilities People Search For Every Day

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Dependencies: None](https://img.shields.io/badge/Dependencies-Zero%20(Standard%20Library)-success.svg)](https://docs.python.org/3/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/abdelrahmanabuzed-onepice/everyday-dev-tools/pulls)

A curated collection of **10 standalone, zero-dependency Python tools** engineered to solve everyday sysadmin, automation, and cybersecurity headaches. Each tool runs out of the box using pure Python without installing heavy packages.

---

## 🧰 The 10 Everyday Tools

| # | Tool Script | What Problem It Solves |
|---|---|---|
| **01** | `01_win_turbo_cleaner.py` | Safely purges temporary user cache, Windows temp junk, and reports megabytes reclaimed. |
| **02** | `02_phishing_link_defanger.py` | Defangs malicious URLs, extracts domain indicators, and flags credential-phishing keywords. |
| **03** | `03_smart_folder_sorter.py` | Instantly sorts messy `Downloads` or `Desktop` folders into organized document/image categories. |
| **04** | `04_fastest_dns_benchmark.py` | Pings Cloudflare, Google, Quad9, and AdGuard to benchmark which resolver gives you the lowest latency. |
| **05** | `05_pdf_text_extractor_merger.py` | Extracts readable text from local PDF files with 100% offline privacy (no cloud uploads). |
| **06** | `06_port_pulse_checker.py` | Rapidly tests whether common service ports (HTTP, HTTPS, SSH, SMTP, RDP) are open or filtered. |
| **07** | `07_csv_excel_deduper.py` | Deduplicates CSV records, trims whitespace, auto-fixes Arabic/Latin encodings, and exports clean datasets. |
| **08** | `08_autorun_persistence_guard.py` | Audits Windows Registry Startup keys to uncover hidden autostart apps or stealth persistence. |
| **09** | `09_password_entropy_auditor.py` | Calculates mathematical Shannon entropy (bits) of passwords and generates uncrackable replacements. |
| **10** | `10_smart_file_backup.py` | Differential backup tool that only syncs new/modified files and verifies integrity using SHA-256. |

---

## 🚀 Quick Start (Zero Setup)

No `pip install` required! Run the interactive master launcher:

```bash
git clone https://github.com/abdelrahmanabuzed-onepice/everyday-dev-tools.git
cd everyday-dev-tools

python main_menu.py
```

*Or execute any standalone tool directly, for example:*
```bash
# Clean junk temp files
python 01_win_turbo_cleaner.py

# Find fastest DNS server
python 04_fastest_dns_benchmark.py

# Audit password entropy
python 09_password_entropy_auditor.py "MyPassw0rd#2026"
```

---

## 👤 Author & Maintainer
**Abdelrahman Abouzed**  
- GitHub: [@abdelrahmanabuzed-onepice](https://github.com/abdelrahmanabuzed-onepice)  
- Email: [abdelrahman.abuzed@gmail.com](mailto:abdelrahman.abuzed@gmail.com)

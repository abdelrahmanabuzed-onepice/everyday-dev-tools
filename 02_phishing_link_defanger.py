"""
Tool 2: Phishing Link & URL Defanger & Analyzer
Defangs suspicious URLs, parses domain and protocol, and checks for typosquatting tricks.
Author: Abdelrahman Abouzed
"""

import re
from urllib.parse import urlparse
import sys


def analyze_and_defang_url(url: str):
    parsed = urlparse(url if "://" in url else "http://" + url)
    domain = parsed.netloc or parsed.path.split("/")[0]
    
    # Defanging
    defanged = re.sub(r'https?://', lambda m: m.group(0).replace('http', 'hxxp'), url, flags=re.IGNORECASE)
    defanged = defanged.replace('.', '[.]')
    defanged = defanged.replace('@', '[at]')
    
    # Simple heuristics
    flags = []
    if "@" in url:
        flags.append("Contains '@' symbol (credential injection / redirect trick)")
    if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', domain):
        flags.append("Host is a raw IP address instead of domain name")
    if domain.count("-") > 2:
        flags.append("Excessive hyphens in domain (possible brand spoofing)")
    if any(k in domain.lower() for k in ["secure", "login", "update", "verify", "banking", "account"]) and not any(legit in domain.lower() for legit in ["google", "microsoft", "apple"]):
        flags.append("Urgent security/banking keyword in untrusted domain")

    return {
        "original": url,
        "defanged": defanged,
        "domain": domain,
        "suspicious_flags": flags,
        "risk_level": "SUSPICIOUS / HIGH" if flags else "LOW / NEUTRAL"
    }


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "http://login-verify-account.bank-update.com@192.168.1.1/invoice.pdf"
    res = analyze_and_defang_url(target)
    print("\n" + "=" * 55)
    print("      PHISHING LINK DEFANGER & ANALYZER")
    print("=" * 55)
    print(f"Original:    {res['original']}")
    print(f"Defanged:    {res['defanged']}")
    print(f"Domain:      {res['domain']}")
    print(f"Risk Rating: {res['risk_level']}")
    if res['suspicious_flags']:
        print("Flags Detected:")
        for f in res['suspicious_flags']:
            print(f"  [!] {f}")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    main()

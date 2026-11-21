"""
Tool 6: Port Pulse Checker
Rapid multi-port scanner for popular services (HTTP, HTTPS, SSH, FTP, RDP, SMTP).
Author: Abdelrahman Abouzed
"""

import socket
import sys
import time

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    465: "SMTPS",
    587: "SMTP Submission",
    3306: "MySQL",
    3389: "RDP (Remote Desktop)",
    8080: "HTTP Alt"
}


def check_port(host: str, port: int, timeout: float = 1.5) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def scan_host(host: str):
    print("\n" + "=" * 55)
    print(f"      PORT PULSE CHECKER: {host}")
    print("=" * 55)

    open_ports = []
    for port, service in COMMON_PORTS.items():
        is_open = check_port(host, port)
        status = "OPEN" if is_open else "CLOSED/FILTERED"
        color_indicator = "[+]" if is_open else "[-]"
        print(f"  {color_indicator} Port {port:<5} ({service:<18}) : {status}")
        if is_open:
            open_ports.append((port, service))

    print("-" * 55)
    print(f"[+] Scan Complete: Found {len(open_ports)} OPEN ports on {host}.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    target_host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    scan_host(target_host)

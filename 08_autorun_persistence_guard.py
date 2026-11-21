"""
Tool 8: Windows Autorun & Persistence Guard
Inspects Windows Registry Run keys and Startup entries to identify autostart programs and stealth persistence.
Author: Abdelrahman Abouzed
"""

import sys
import subprocess
import json


def get_startup_entries():
    ps_cmd = """
    $entries = @()
    $paths = @(
        "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
        "HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    )
    foreach ($p in $paths) {
        if (Test-Path $p) {
            $props = (Get-ItemProperty $p).PSObject.Properties
            foreach ($pr in $props) {
                if ($pr.Name -notmatch "^(PSPath|PSParentPath|PSChildName|PSDrive|PSProvider)$") {
                    $entries += [PSCustomObject]@{
                        Location = $p
                        Name = $pr.Name
                        Command = $pr.Value
                    }
                }
            }
        }
    }
    $entries | ConvertTo-Json
    """
    try:
        out = subprocess.check_output(["powershell", "-NoProfile", "-Command", ps_cmd], text=True, stderr=subprocess.DEVNULL)
        if out.strip():
            data = json.loads(out)
            return data if isinstance(data, list) else [data]
    except Exception:
        pass
    return []


def audit_autoruns():
    print("\n" + "=" * 55)
    print("      WINDOWS AUTORUN & STARTUP PERSISTENCE AUDITOR")
    print("=" * 55)
    entries = get_startup_entries()
    print(f"[*] Found {len(entries)} configured Startup / Run entries:\n")

    for idx, e in enumerate(entries, 1):
        name = e.get("Name", "Unknown")
        cmd = e.get("Command", "Unknown")
        loc = "User" if "HKCU" in e.get("Location", "") else "System (HKLM)"
        print(f" [{idx}] [{loc}] {name}")
        print(f"     Path: {cmd}")

    print("=" * 55 + "\n")


if __name__ == "__main__":
    audit_autoruns()

"""
Tool 4: Fastest DNS Benchmark & Latency Tester
Benchmarks popular public DNS resolvers and recommends the fastest server for your connection.
Author: Abdelrahman Abouzed
"""

import socket
import time

DNS_SERVERS = [
    ("Cloudflare", "1.1.1.1"),
    ("Google", "8.8.8.8"),
    ("Quad9 Security", "9.9.9.9"),
    ("OpenDNS", "208.67.222.222"),
    ("AdGuard DNS", "94.140.14.14"),
    ("Level3", "4.2.2.2")
]


def test_dns_latency(ip: str, port: int = 53, runs: int = 3) -> float:
    latencies = []
    for _ in range(runs):
        start = time.time()
        try:
            with socket.create_connection((ip, port), timeout=2.0):
                lat = (time.time() - start) * 1000.0
                latencies.append(lat)
        except Exception:
            pass
        time.sleep(0.05)
        
    if latencies:
        return round(sum(latencies) / len(latencies), 1)
    return 9999.0


def run_benchmark():
    print("\n" + "=" * 55)
    print("      FASTEST DNS RESOLVER BENCHMARK")
    print("=" * 55)
    
    results = []
    for name, ip in DNS_SERVERS:
        print(f"[*] Testing {name:<18} ({ip:<15})...", end="", flush=True)
        avg_ms = test_dns_latency(ip)
        if avg_ms < 9000:
            print(f" {avg_ms:>6.1f} ms")
            results.append((avg_ms, name, ip))
        else:
            print(" TIMEOUT")
            
    print("-" * 55)
    if results:
        results.sort()
        fastest = results[0]
        print(f"🏆 FASTEST RESOLVER: {fastest[1]} ({fastest[2]}) with {fastest[0]} ms latency!")
        print("\nLeaderboard:")
        for rank, (lat, name, ip) in enumerate(results, 1):
            print(f"  #{rank}  {name:<18} : {lat} ms")
    else:
        print("[!] No DNS servers responded.")
    print("=" * 55 + "\n")


if __name__ == "__main__":
    run_benchmark()

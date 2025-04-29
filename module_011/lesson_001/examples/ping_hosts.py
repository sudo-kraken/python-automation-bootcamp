# Example script: ping_hosts.py
import subprocess

# Ask the user for a list of hosts
hosts_input = input("Enter hostnames or IPs to ping (separated by commas): ")
hosts = [h.strip() for h in hosts_input.split(",") if h.strip()]

# Ping each host once and report the result
for host in hosts:
    print(f"Pinging {host}...")
    # Use -c 1 for Unix/Linux/Mac (one ping), or -n 1 for Windows
    try:
        # Try with -c 1 (Unix-like)
        result = subprocess.run(["ping", "-c", "1", host],
                                capture_output=True, text=True)
    except Exception:
        # If the above fails (possibly on Windows), try -n 1
        result = subprocess.run(["ping", "-n", "1", host],
                                capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{host} is reachable.")
    else:
        print(f"{host} is NOT reachable.")

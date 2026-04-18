import socket

target = input("Enter target IP: ")

open_ports = []

print(f"\nScanning {target}...\n")

for port in range(20, 200):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.3)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")
        open_ports.append(port)

    sock.close()

# ✅ ADD THIS LINE RIGHT HERE
print(f"\nTotal Open Ports: {len(open_ports)}")

# Save report
with open("scan_report.txt", "w") as f:
    f.write(f"Scan Results for {target}\n")
    f.write("-------------------------\n")

    if open_ports:
        for port in open_ports:
            f.write(f"Port {port} is OPEN\n")
    else:
        f.write("No open ports found\n")

print("\nScan complete. Report saved as scan_report.txt")
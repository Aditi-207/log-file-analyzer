import socket
import tkinter as tk

def scan_ports():
    target = entry.get()
    output.delete("1.0", tk.END)

    if not target:
        output.insert(tk.END, "Please enter a target IP\n")
        return

    open_ports = []

    output.insert(tk.END, f"Scanning {target}...\n\n")

    for port in range(20, 200):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)

        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)
            output.insert(tk.END, f"Port {port} is OPEN\n")

        sock.close()

    output.insert(tk.END, f"\nTotal Open Ports: {len(open_ports)}\n")
    output.insert(tk.END, "Scan Complete")

# GUI setup
root = tk.Tk()
root.title("Network Scanner Tool")
root.geometry("500x400")

tk.Label(root, text="Enter Target IP:").pack()

entry = tk.Entry(root, width=40)
entry.pack()

tk.Button(root, text="Scan Ports", command=scan_ports).pack(pady=10)

output = tk.Text(root, height=15, width=60)
output.pack()

root.mainloop()
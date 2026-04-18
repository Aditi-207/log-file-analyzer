import tkinter as tk
from tkinter import filedialog, messagebox

def analyze_logs(file_path):
    failed_logins = 0
    suspicious_ips = []
    user_attempts = {}

    with open(file_path, "r") as file:
        for line in file:
            if "Failed login attempt" in line:
                failed_logins += 1
                user = line.split(":")[-1].strip()
                user_attempts[user] = user_attempts.get(user, 0) + 1
            
            if "Suspicious IP" in line:
                ip = line.split(":")[-1].strip()
                suspicious_ips.append(ip)

    result = "---- Security Report ----\n"
    result += f"Total Failed Logins: {failed_logins}\n"

    for user, count in user_attempts.items():
        if count >= 3:
            result += f"ALERT: Brute force attack on {user} ({count} attempts)\n"

    if suspicious_ips:
        result += "Suspicious IPs:\n"
        for ip in suspicious_ips:
            result += f"- {ip}\n"

    return result


def select_file():
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)


def run_analysis():
    file_path = entry.get()

    if not file_path:
        messagebox.showerror("Error", "Please select a log file")
        return

    result = analyze_logs(file_path)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

    with open("report.txt", "w") as f:
        f.write(result)


# GUI setup
root = tk.Tk()
root.title("Log Analyzer - Cybersecurity Tool")
root.geometry("500x400")

tk.Label(root, text="Select Log File:").pack()

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Browse", command=select_file).pack(pady=5)
tk.Button(root, text="Analyze Logs", command=run_analysis).pack(pady=5)

output_text = tk.Text(root, height=15, width=60)
output_text.pack()

root.mainloop()
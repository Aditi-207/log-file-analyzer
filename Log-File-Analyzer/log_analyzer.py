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

    print("---- Security Report ----")
    print(f"Total Failed Logins: {failed_logins}")

    # Brute force detection
    for user, count in user_attempts.items():
        if count >= 3:
            print(f"ALERT: Possible brute force attack on user '{user}' ({count} attempts)")

    if suspicious_ips:
        print("Suspicious IPs:")
        for ip in suspicious_ips:
            print(f"- {ip}")

    # Save report
    with open("report.txt", "w") as report:
        report.write("---- Security Report ----\n")
        report.write(f"Total Failed Logins: {failed_logins}\n")

        for user, count in user_attempts.items():
            if count >= 3:
                report.write(f"ALERT: Brute force on {user} ({count} attempts)\n")

        if suspicious_ips:
            report.write("Suspicious IPs:\n")
            for ip in suspicious_ips:
                report.write(f"- {ip}\n")

    print("\nReport saved as report.txt")

analyze_logs("logs.txt")
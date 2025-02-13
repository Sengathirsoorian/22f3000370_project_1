import json
import datetime

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def format_file(file_path):
    import subprocess
    subprocess.run(["npx", "prettier", "--write", file_path], check=True)
    return f"Formatted {file_path}"

def count_wednesdays(file_path):
    with open(file_path, "r") as file:
        dates = file.readlines()
    count = sum(1 for date in dates if datetime.datetime.strptime(date.strip(), "%Y-%m-%d").weekday() == 2)
    with open("/data/dates-wednesdays.txt", "w") as out_file:
        out_file.write(str(count))
    return f"Wednesdays count written to /data/dates-wednesdays.txt"

def sort_contacts(file_path):
    with open(file_path, "r") as file:
        contacts = json.load(file)
    contacts.sort(key=lambda x: (x["last_name"], x["first_name"]))
    with open("/data/contacts-sorted.json", "w") as out_file:
        json.dump(contacts, out_file, indent=4)
    return "Contacts sorted"

def extract_logs(file_path):
    with open(file_path, "r") as file:
        logs = file.readlines()
    error_logs = [log for log in logs if "ERROR" in log]
    with open("/data/error-logs.txt", "w") as out_file:
        out_file.writelines(error_logs)
    return "Error logs extracted"
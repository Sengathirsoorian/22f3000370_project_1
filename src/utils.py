import json
import datetime

def extract_dates(dates, target_weekday):
    count = 0
    for date in dates:
        parsed_date = datetime.datetime.strptime(date.strip(), "%Y-%m-%d")
        if parsed_date.strftime("%A") == target_weekday:
            count += 1
    return count

def sort_contacts(task):
    input_path = "/data/contacts.json"
    output_path = "/data/contacts-sorted.json"

    with open(input_path, "r") as f:
        contacts = json.load(f)

    sorted_contacts = sorted(contacts, key=lambda x: (x["last_name"], x["first_name"]))

    with open(output_path, "w") as f:
        json.dump(sorted_contacts, f, indent=4)

    return {"status": "success", "message": "Contacts sorted successfully"}

def extract_headers(task):
    input_dir = "/data/docs/"
    output_path = "/data/docs/index.json"

    headers = {}
    for file in os.listdir(input_dir):
        if file.endswith(".md"):
            with open(os.path.join(input_dir, file), "r") as f:
                for line in f:
                    if line.startswith("# "):
                        headers[file] = line.strip("# ").strip()
                        break

    with open(output_path, "w") as f:
        json.dump(headers, f, indent=4)

    return {"status": "success", "message": "Markdown index created"}

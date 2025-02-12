import os
import subprocess
import json
import datetime
from src.utils import extract_dates, sort_contacts, extract_headers
from src.llm_helper import query_llm

DATA_PATH = "/data/"

def execute_task(task: str):
    """
    Parses the task and executes the appropriate function.
    """
    if "install uv" in task and "datagen.py" in task:
        return install_uv_and_run_datagen(task)
    elif "format" in task and "prettier" in task:
        return format_file_with_prettier(task)
    elif "count Wednesdays" in task:
        return count_weekdays(task, "Wednesday")
    elif "sort contacts" in task:
        return sort_contacts(task)
    elif "most recent log files" in task:
        return process_recent_logs(task)
    elif "extract Markdown headers" in task:
        return index_markdown_headers(task)
    elif "extract email sender" in task:
        return extract_email_sender(task)
    elif "extract credit card" in task:
        return extract_credit_card_number(task)
    elif "find similar comments" in task:
        return find_similar_comments(task)
    elif "calculate ticket sales" in task:
        return calculate_ticket_sales(task)
    else:
        return {"status": "error", "error": "Task not recognized"}

# Example of one task function
def count_weekdays(task: str, weekday: str):
    file_path = os.path.join(DATA_PATH, "dates.txt")
    output_path = os.path.join(DATA_PATH, "dates-wednesdays.txt")

    try:
        with open(file_path, "r") as f:
            dates = f.readlines()

        count = extract_dates(dates, weekday)

        with open(output_path, "w") as f:
            f.write(str(count))

        return {"status": "success", "message": f"Counted {count} {weekday}s"}
    except Exception as e:
        return {"status": "error", "error": str(e)}

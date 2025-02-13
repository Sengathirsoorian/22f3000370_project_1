import os
import logging
import json
from src.llm_utils import parse_task
from src.file_utils import format_file, count_wednesdays, sort_contacts, extract_logs
from src.security import enforce_security

logging.basicConfig(level=logging.INFO)

def execute_task(task: str):
    logging.info(f"Executing task: {task}")
    try:
        parsed_task = parse_task(task)
        logging.info(f"Parsed task: {parsed_task}")
        
        if not enforce_security(parsed_task):
            raise ValueError("Security violation detected!")

        task_type = parsed_task.get("type")
        file_path = parsed_task.get("file")

        logging.info(f"Task type: {task_type}, File path: {file_path}")

        if task_type == "format":
            return format_file(file_path)
        elif task_type == "count_wednesdays":
            return count_wednesdays(file_path)
        elif task_type == "sort_contacts":
            return sort_contacts(file_path)
        elif task_type == "extract_logs":
            return extract_logs(file_path)
        else:
            raise ValueError("Unknown task type")
    except Exception as e:
        logging.error(f"Error executing task: {e}")
        raise 
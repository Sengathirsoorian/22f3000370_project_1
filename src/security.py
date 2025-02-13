import os

def enforce_security(task):
    if ".." in task.get("file", "") or not task["file"].startswith("/data/"):
        return False
    return True

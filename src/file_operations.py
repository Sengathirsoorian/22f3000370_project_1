import os

DATA_PATH = "/data/"

def read_file(path: str):
    """
    Reads the content of a file.
    """
    full_path = os.path.join(DATA_PATH, path.strip("/"))
    
    if not os.path.exists(full_path):
        raise FileNotFoundError("File does not exist")

    with open(full_path, "r") as f:
        return f.read()

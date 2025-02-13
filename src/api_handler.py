import requests

def fetch_api_data(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "w") as file:
            file.write(response.text)
        return f"Saved API data to {save_path}"
    else:
        return "Failed to fetch API data"

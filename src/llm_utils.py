import openai
import os
import json

# Set your valid Copilot API key here
openai.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDAzNzBAZHMuc3R1ZHkuaWl0bS5pbiJ9.9twvpeQUDu12wkE4IdYEisdVXz1Q0ZSfnRkRiVTkaNg"

# Set the base URL for the OpenAI API to use the proxy
openai.api_base = "https://aiproxy.sanand.workers.dev/openai/v1"

def parse_task(task: str):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract the key details from this task."},
            {"role": "user", "content": task}
        ]
    )
    
    content = response["choices"][0]["message"]["content"]
    # Assuming the response content is a JSON string, parse it into a dictionary
    parsed_task = json.loads(content)
    return parsed_task


import os
import openai

API_KEY = os.environ.get("eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDAzNzBAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.9twvpeQUDu12wkE4IdYEisdVXz1Q0ZSfnRkRiVTkaNg")

def query_llm(prompt: str):
    """
    Sends a prompt to GPT-4o-Mini and returns the extracted result.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        api_key=API_KEY
    )
    return response["choices"][0]["message"]["content"].strip()

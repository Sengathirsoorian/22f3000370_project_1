import openai
import os
from sentence_transformers import util

# Set your valid Copilot API key here
openai.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDAzNzBAZHMuc3R1ZHkuaWl0bS5pbiJ9.9twvpeQUDu12wkE4IdYEisdVXz1Q0ZSfnRkRiVTkaNg"

# Set the base URL for the OpenAI API to use the proxy
openai.api_base = "https://aiproxy.sanand.workers.dev/openai/v1"

def find_similar_comments(file_path):
    with open(file_path, "r") as file:
        comments = file.readlines()
    
    response = openai.Embedding.create(
        model="text-embedding-3-small",
        input=comments
    )
    
    embeddings = [data["embedding"] for data in response["data"]]
    max_sim = -1
    best_pair = None
    
    for i in range(len(comments)):
        for j in range(i + 1, len(comments)):
            similarity = util.pytorch_cos_sim(embeddings[i], embeddings[j]).item()
            if similarity > max_sim:
                max_sim = similarity
                best_pair = (comments[i], comments[j])
    
    with open("/data/comments-similar.txt", "w") as file:
        file.write("\n".join(best_pair))
    
    return "Similar comments saved"
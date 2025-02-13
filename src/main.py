from fastapi import FastAPI, HTTPException
from src.executor import execute_task
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.post("/run")
async def run_task(task: str):
    try:
        logging.info(f"Received task: {task}")
        result = execute_task(task)
        logging.info(f"Task result: {result}")
        return {"result": result}
    except Exception as e:
        logging.error(f"Error executing task: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
async def read_file(path: str):
    try:
        with open(path, "r") as file:
            content = file.read()
        return {"content": content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
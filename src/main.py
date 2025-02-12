from fastapi import FastAPI, HTTPException, Query
from src.task_executor import execute_task
from src.file_operations import read_file

app = FastAPI()

@app.post("/run")
def run_task(task: str = Query(..., description="Task description in plain English")):
    try:
        result = execute_task(task)
        if result["status"] == "success":
            return {"message": "Task executed successfully", "details": result}
        else:
            raise HTTPException(status_code=400, detail=result["error"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/read")
def read_file_content(path: str = Query(..., description="File path to read")):
    try:
        content = read_file(path)
        return {"file_path": path, "content": content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

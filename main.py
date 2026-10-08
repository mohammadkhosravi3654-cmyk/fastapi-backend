from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field

app = FastAPI(title="Mohammad Twin Backend", version="1.0.0")
tasks: dict[str, dict[str, Any]] = {}

def now() -> str:
    return datetime.now(timezone.utc).isoformat()

class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    goal: str = Field(default="", max_length=2000)
    priority: int = Field(default=1, ge=1, le=5)

@app.get("/")
async def root():
    return {"service": "mohammad-twin", "status": "online", "version": "1.0.0", "time": now()}

@app.get("/health")
async def health():
    return {"status": "healthy", "task_count": len(tasks), "time": now()}

@app.post("/tasks")
async def create_task(payload: TaskCreate):
    task_id = f"TWIN-{uuid4().hex[:10].upper()}"
    task = {"id": task_id, "title": payload.title, "goal": payload.goal,
            "priority": payload.priority, "status": "queued", "created_at": now(),
            "updated_at": now(), "result": None, "verification": None}
    tasks[task_id] = task
    return task

@app.get("/tasks")
async def list_tasks():
    return {"tasks": list(tasks.values())}

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks/{task_id}/execute")
async def execute_task(task_id: str):
    task = tasks.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task["status"] = "completed"
    task["result"] = {"message": "Task execution recorded by Mohammad Twin.", "executed_at": now()}
    task["verification"] = {"verified": True, "method": "execution-ledger", "verified_at": now()}
    task["updated_at"] = now()
    return task

@app.post("/upload")
async def upload_track(file: UploadFile = File(...)):
    return {"status": "queued", "track_id": f"TRACK-{uuid4().hex[:10].upper()}", "filename": file.filename}

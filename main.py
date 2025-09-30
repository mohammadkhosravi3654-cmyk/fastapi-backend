from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API is working ✅"}

@app.post("/upload")
async def upload_track(file: UploadFile = File(...)):
    return {
        "status": "queued",
        "track_id": "TRACK_123",
        "filename": file.filename
    }
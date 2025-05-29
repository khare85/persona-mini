from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import List
import os

from core.parser import parse_resume
from core.embedder import get_embedding
from core.matcher import match_job_description

app = FastAPI(title="Resume Matcher API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class JobMatchRequest(BaseModel):
    job_description: str

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())

    try:
        content = parse_resume(file_path)
        vector = get_embedding(content)

        point_id = hash(file.filename) % 100000

        from app.database import client, COLLECTION_NAME
        from qdrant_client.http.models import PointStruct

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=point_id,
                    vector=vector,
                    payload={"filename": file.filename, "content": content[:1000]}
                )
            ]
        )

        return {"message": "Resume uploaded", "filename": file.filename}
    except Exception as e:
        return {"error": str(e)}

@app.post("/match-job")
async def match_job(req: JobMatchRequest):
    matches = match_job_description(req.job_description)
    return {"matches": matches}
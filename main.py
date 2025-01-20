from fastapi import FastAPI, HTTPException
from models import ProcessRequest, ProcessResponse
from services import process_text

app = FastAPI()

@app.post("/process")
async def process_text_route(data: ProcessRequest):
    try:
        result = process_text(data.text)
        return ProcessResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

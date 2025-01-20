from fastapi import FastAPI, HTTPException
from models import ProcessRequest, ProcessResponse
from services import process_text

app = FastAPI()
history = []

@app.post("/process")
async def process_text_route(data: ProcessRequest):
    try:
        result = process_text(data.text)
        history.append({"input": data.text, "result": result})
        return ProcessResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    return history

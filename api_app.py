from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
import pandas as pd
from parser import load_data
from visualizer import generate_charts
import os
import zipfile

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "uploaded": False,
        "chart_info": []
    })

@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile = File(...)):
    filepath = f"sample_data/{file.filename}"
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = load_data(filepath)
    chart_info = generate_charts(df)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "chart_info": chart_info,
        "uploaded": True
    })

@app.get("/download_zip")
def download_zip():
    zip_filename = "charts.zip"
    zip_path = f"./{zip_filename}"

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in os.listdir("outputs"):
            if file.endswith(".png"):
                zipf.write(os.path.join("outputs", file), arcname=file)

    return FileResponse(zip_path, filename=zip_filename, media_type='application/zip')

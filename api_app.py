from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from parser import load_data
from analyzer import analyze_data
from visualizer import generate_visualizations
import os, shutil

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload(request: Request, file: UploadFile = File(...)):
    path = f"sample_data/{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = load_data(path)
    insights = analyze_data(df)
    generate_visualizations(df, insights)

    images = os.listdir("outputs")
    return templates.TemplateResponse("index.html", {
        "request": request,
        "images": images,
        "message": "Charts generated successfully!"
    })

@app.get("/chart/{name}")
def get_image(name: str):
    return FileResponse(f"outputs/{name}")
from fastapi import FastAPI, UploadFile, File
from parser import load_data
from analyzer import analyze_data
from visualizer import generate_visualizations
import os, shutil

app = FastAPI()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    input_path = f"sample_data/{file.filename}"
    
    # Save uploaded file
    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Load and analyze
    df = load_data(input_path)
    insights = analyze_data(df)
    generate_visualizations(df, insights)

    return {
        "status": "success",
        "outputs": os.listdir("outputs/")
    }
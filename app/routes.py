from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import openai
import pandas as pd
from PyPDF2 import PdfReader
from io import BytesIO
import os

router = APIRouter()

# Initialize the OpenAI API client with the provided API key
client = openai.Client(api_key='put open api key')

def read_pdf(file):
    try:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process PDF file: {e}")

def detect_and_summarize_sections(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": 
                    "Please analyze the following CV text. Identify the key sections such as Personal Information, Summary, Core Competencies, Professional Experience, Education, Skills, Languages, and Publications. For each section, provide a summary in no more than two sentences. Format the output as: Section Name: Summary."},
                {"role": "user", "content": text}
            ]
        )
        sections = response.choices[0].message.content.strip()
        return sections
    except openai.error.OpenAIError as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {e}")

@router.post("/extract_key_points/")
async def extract_key_points_endpoint(file: UploadFile = File(...)):
    pdf_file = BytesIO(await file.read())
    text = read_pdf(pdf_file)
    
    sections = detect_and_summarize_sections(text)
    labeled_sections = sections.split("\n\n")
    
    summaries = []

    for labeled_section in labeled_sections:
        # Check if the section contains a colon to split
        if ":" in labeled_section:
            label, section_text = labeled_section.split(":", 1)
            summaries.append({"Section": label.strip(), "Summary": section_text.strip()})
        else:
            # Log unexpected formats for debugging
            print(f"Skipping section due to unexpected format: {labeled_section}")
            continue

    if not summaries:
        raise HTTPException(status_code=500, detail="No valid sections were found or summarized.")

    df = pd.DataFrame(summaries)
    output_filename = "summaries_output.xlsx"
    df.to_excel(output_filename, index=False)
    
    return {"summaries": summaries, "filename": output_filename}

@router.get("/download_excel/")
async def download_excel_file(filename: str):
    file_path = os.path.join(os.getcwd(), filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(path=file_path, filename=filename, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

import os
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract
import cv2

def parse_pdf(path):
    with open(path, 'rb') as f:
        return "\n".join([page.extract_text() for page in PdfReader(f).pages])

def parse_docx(path):
    doc = Document(path)
    return "\n".join(para.text for para in doc.paragraphs)

def parse_txt(path):
    with open(path, 'r') as f:
        return f.read()

def ocr_image(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    return pytesseract.image_to_string(Image.fromarray(binary))

def parse_resume(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        return parse_pdf(path)
    elif ext == ".docx":
        return parse_docx(path)
    elif ext == ".txt":
        return parse_txt(path)
    elif ext in [".jpg", ".jpeg", ".png"]:
        return ocr_image(path)
    else:
        raise ValueError("Unsupported file format")
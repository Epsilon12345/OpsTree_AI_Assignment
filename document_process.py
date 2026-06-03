from PyPDF2 import PdfReader
from docx import Document

def read_pdf(file):
    text=""
    pdf=PdfReader(file)

    for page in pdf.pages:
        text+= page.extract_text() +'\n'

    return text

def read_docx(file):
    doc=Document(file)
    text="\n".join(para.text for para in doc.paragraphs)
    return text

def read_txt(file):
    return file.read().decode("UTF-8")

def chunking(text, chunk_size=390):
    chunks=[]

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    return chunks



from fastapi import FastAPI, UploadFile, File,APIRouter
from fastapi.responses import JSONResponse
import PyPDF2

from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
# from langchain_community.document_loaders import PyPDFLoader
load_dotenv()
from io import BytesIO
router = APIRouter(prefix="/resume", tags=["Resume"])
# Load the Groq LLM
model = ChatGroq(
    temperature=0.7,
    model_name="llama3-8b-8192"  # You can also try "llama3-8b-8192"
)
@router.post("/upload-resume/")
async def upload_resume(resume: UploadFile = File(...)):
    if not resume.filename.endswith(".pdf"):
        return JSONResponse(content={"error": "Only PDF files are supported."}, status_code=400)

    # Load PDF from memory using PyPDF2
    pdf_reader = PyPDF2.PdfReader(BytesIO(await resume.read()))
    full_text = ""

    for page in pdf_reader.pages:
        full_text += page.extract_text() + "\n"

    return {"resume_text": full_text.strip()}

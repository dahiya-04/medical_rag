import os
from dotenv import load_dotenv

HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

MODEL_NAME = "llama-3.1-8b-instant"

HUGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
db_faiss_path ="vectorstore/db_faiss"
data_path = "data/"
chunk_size = 500
chunk_overlap = 50
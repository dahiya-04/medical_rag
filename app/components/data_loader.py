import os
from app.components.pdf_loader import load_pdf,create_text_chunks
from app.components.vector_store import create_vector_store,load_vector_store
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import db_faiss_path

logger = get_logger(__name__)

def process_and_store_pdfs():

    try:
        logger.info("main function started: processing and storing PDFs...")
        documents = load_pdf()
        text_chunks = create_text_chunks(documents)
        create_vector_store(text_chunks)
       
        logger.info("main vector store creation completed successfully.")
    except Exception as e:
        logger.error(f"Error in vector store creation function: {str(e)}")
        raise CustomException(f"Error in main function: {str(e)}")


if __name__ == "__main__":
    process_and_store_pdfs()
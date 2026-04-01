from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embeddings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
import os
from app.config.config import db_faiss_path
logger = get_logger(__name__)


def load_vector_store():
    """Load the vector store from disk."""
    try:
        logger.info("Loading vector store from disk...")
        embeddings_model = get_embeddings()
        if os.path.exists(db_faiss_path):
            vector_store = FAISS.load_local(db_faiss_path, embeddings_model,allow_dangerous_code_execution=True)
            logger.info("Vector store loaded successfully.")
            return vector_store
        else:
            logger.warning("Vector store not found. Returning None.")
            return None
    except Exception as e:
        error_message = CustomException(f"Error loading vector store: {str(e)}")
        logger.error(error_message)
        raise error_message

def create_vector_store(text_chunks):
    """creating new vector store and saving it to disk."""
    try:
        if not text_chunks:
            logger.warning("No text chunks provided. Skipping vector store creation.")
            raise CustomException("No text chunks provided for vector store creation.")
        logger.info("Creating new vector store...")
        embeddings_model = get_embeddings()
        db = FAISS.from_documents(text_chunks, embeddings_model)
        db.save_local(db_faiss_path)
        logger.info("Vector store saved successfully.")
        return db
    except Exception as e:
        error_message = CustomException(f"Error saving vector store: {str(e)}")
        logger.error(error_message)
        raise error_message

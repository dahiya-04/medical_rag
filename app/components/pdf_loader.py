import os
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import chunk_size,chunk_overlap,data_path

logger=get_logger(__name__)

def load_pdf():
    """Load PDF files from the specified data path and return a list of documents."""
    try:
        if not os.path.exists(data_path):
            raise CustomException(f"Data path {data_path} does not exist.")

        logger.info(f"Loading PDF files from {data_path}...")
        loader =DirectoryLoader(data_path, glob="*.pdf", show_progress=True, loader_cls=PyPDFLoader)
        documents = loader.load()
        if not documents:
            logger.warning(f"No PDF documents found in {data_path}.")
        logger.info(f"Loaded {len(documents)} documents.")
        return documents
    except Exception as e:
        logger.error(f"Error loading PDF files: {str(e)}")
        raise CustomException(f"Error loading PDF files: {str(e)}")



def create_text_chunks(documents):
    """Split the loaded documents into text chunks and return a list of chunks."""
    try:
        if not documents:
            raise CustomException("No documents to create text chunks from.")

        logger.info(f"splitting documents into chunks with chunk size {chunk_size} and chunk overlap {chunk_overlap}...")
        text_splitter=RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        text_chunks=text_splitter.split_documents(documents)
        logger.info(f"Created {len(text_chunks)} text chunks.")
        return text_chunks

    except Exception as e:
        logger.error(f"Error creating text chunks: {str(e)}")
        raise CustomException(f"Error creating text chunks: {str(e)}")

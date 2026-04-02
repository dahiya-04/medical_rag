from langchain_groq import ChatGroq
from app.config.config import GROQ_API_KEY

from app.common.logger import get_logger
from app.common.custom_exception import CustomException
logger = get_logger(__name__)

def load_llm():
    """Load the language model using the provided API key."""
    try:
        logger.info("Loading language model...")
        if not GROQ_API_KEY:GROQ_API_KEY
            raise CustomException("Groq API key is not set. Please set the GROQ_API_KEY environment variable.")
        llm = ChatGroq(api_key=GROQ_API_KEY,model_name = "llama-3.1-8b-instant",temperature=0,max_tokens=2048)
        logger.info("Language model loaded successfully.")
        return llm
    except Exception as e:
        error_message = CustomException(f"Error loading language model: {str(e)}")
        logger.error(error_message)
        raise error_message
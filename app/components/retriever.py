from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from app.compenents.llm import load_llm
from app.components.vector_store import load_vector_store
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from app.config.config import HUGINGFACE_REPO_ID,HF_TOKEN,GROQ_API_KEY

import os

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """ Answer the following medical question in 2-3 lines maximum using only the information provided in the context.

Context:
{context}

Question:
{question}

Answer:
"""
def set_custom_prompt():
    return PromptTemplate(template=CUSTOM_PROMPT_TEMPLATE, input_variables=["context", "question"])

def create_qa_chain():
    try:
        logger.info("loading vector store...")
        db = load_vector_store()
        llm=load_llm()
        if db is None:
            logger.warning("Vector store is not available. Cannot create QA chain.")
            raise CustomException("Vector store is not available for QA chain creation.")
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=db.as_retriever(search_kwargs={"k": 2}),
            return_source_documents=False,
            chain_type_kwargs={"prompt": set_custom_prompt()}
        )
        logger.info("QA chain created successfully.")
        return qa_chain
    except Exception as e:
        logger.error(f"Error occurred while creating QA chain: {str(e)}")
        raise CustomException("Failed to create QA chain.")
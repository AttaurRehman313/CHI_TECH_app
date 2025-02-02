from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from mainapp.utils.file_loadin_and_chunking import create_chunks
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

"""
This line initializes the Google Generative AI Embeddings model using the specified embedding model, 
'models/embedding-001'.
This embedding model will likely be used to convert text data into high-dimensional 
vectors suitable for tasks like similarity search or machine learning workflows. 
"""
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=api_key)
def vector_embedding(raw_text):   
    vectorestore =FAISS.from_documents(raw_text, embeddings)
    return vectorestore



def create_vector_db(data):
    """
    This function creates a FAISS-based vector database from the provided data.
    
    The input `data` is processed into manageable chunks using the `create_chunks` function.
    Each chunk is transformed into vector embeddings using the `vector_embedding` function.
    The embeddings are saved locally as a FAISS index file named "faiss_index".
    """
    raw_text=create_chunks(data)
    vector=vector_embedding(raw_text)
    vec_db=vector.save_local("faiss_index")
    return vec_db



def retrievers():
    """
    Loads a pre-built FAISS vector index from the local directory.
    This facilitates efficient similarity searches using vector embeddings.
     """
    vector = FAISS.load_local("faiss_index",embeddings,allow_dangerous_deserialization=True)

    """
    Configures the loaded vector index as a retriever.
    The retriever uses Maximum Marginal Relevance (MMR) to prioritize diverse results.
    """
    retriever = vector.as_retriever(
            search_type="mmr",  # Also test "similarity"
            search_kwargs={"k": 8},
        )

    return retriever
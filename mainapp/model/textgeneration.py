from langchain_google_genai import GoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

def chat_model(retriever):
        """
        This function initializes a Google Generative AI model and configures it with the provided API key.
        It sets up conversation memory to track the chat history,
        ensuring that messages are returned in the correct order.
         
        A ConversationalRetrievalChain is created by combining the language model, retriever, and memory, enabling seamless interaction.
        The chain is then returned, ready to handle user queries and retrieve relevant conversation context.
        """
        llm=llm = GoogleGenerativeAI(model="gemini-2.0-flash-exp",google_api_key=api_key)
        memory=ConversationBufferMemory(memory_key='chat_history',return_messages=True,input_key="question")
        question=ConversationalRetrievalChain.from_llm(    llm=llm,
                                                            retriever=retriever,
                                                            memory=memory,
                                                            get_chat_history=lambda h: h)
        return question



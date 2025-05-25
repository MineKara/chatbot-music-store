import os
from langchain_openai import OpenAI
from langchain.chains.combine_documents.stuff import create_stuff_documents_chain
from langchain_core.prompts import PromptTemplate
from langchain.schema import Document
from data import products
from dotenv import load_dotenv
load_dotenv()

# Set your OpenAI API key (you can also set this as an environment variable)
OPENAI_API_KEY = os.getenv("api_key")

llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# Prepare product info as documents
product_docs = [
    Document(page_content=f"Name: {p['name']}, Specs: {p['specs']}, Price: {p['price']}, Location: {p['store_location']}")
    for p in products
]

# Define the prompt template for the stuff chain
prompt_template = """Answer the following question based on the provided context:

Context: {context}

Question: {question}

Answer:"""
prompt = PromptTemplate.from_template(prompt_template)

# Create the stuff chain using the new constructor
stuff_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)

def answer_user_question(user_question: str) -> str:
    """
    Takes a user question, uses OpenAI to generate a response, and uses the products list for context.
    """
    # Use the StuffDocumentsChain to answer the question with product context
    # The way to invoke the chain also changes slightly
    response = stuff_chain.invoke(
        input={
            "question": user_question,
            "context": product_docs # Pass documents as 'context'
        }
    )
    return response 
from fastapi import FastAPI
from pydantic import BaseModel # Added for request body
from data import products # Import products
from chat import answer_user_question # Import the chat function

app = FastAPI()

# Define request body model
class QuestionRequest(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Chatbot API is running"}

@app.get("/products/7strings")
async def get_7_string_guitars():
    seven_string_products = [
        {
            "name": product["name"],
            "store_location": product["store_location"],
            "price": product["price"],
            "image_url": product["image_url"],
            "specs": product["specs"]
        }
        for product in products
        if product.get("string_count") == 7 and product.get("stock_quantity", 0) > 0
    ]
    return seven_string_products

@app.post("/ask")
async def ask_chatbot(request: QuestionRequest):
    response = answer_user_question(request.question)
    return {"answer": response} 
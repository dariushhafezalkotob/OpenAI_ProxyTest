from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

# Load your OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

# Define a POST route for the chat endpoint
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    messages = data.get("messages", [])

    try:
        # Send messages to OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return JSONResponse(content=response)
    except Exception as e:
        # If an error occurs, return it as a JSON response
        return JSONResponse(content={"error": str(e)}, status_code=500)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
import os

api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not set in environment variables")

# Pass it to the client
client = Groq(api_key=api_key)
class chatRequest(BaseModel):
    message : str
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

#@app.get("/chat")
def get_bot_response(user_message):
    message=user_message.lower()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )

    return chat_completion.choices[0].message.content




@app.post("/chat")
async def chat(request:chatRequest):
    reply = get_bot_response(request.message)
    return {"reply":reply}


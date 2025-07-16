from openai import OpenAI
from models.message import Message as MessageModel
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

class MessageService():
    def __init__(self, db):
        self.db = db

    def chat_with_user(self, user_id: int, content: str):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Sos un asistente virtual argentino"},
                {"role": "user", "content": content}
            ]
        )
        reply = response.choices[0].message.content
        msg = MessageModel(user_id=user_id, content=content, response=reply)
        self.db.add(msg)
        self.db.commit()
        self.db.refresh(msg)
        return msg

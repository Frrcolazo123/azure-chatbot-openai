# from openai import OpenAI
# from models.message import Message
# from sqlalchemy.orm import Session
# import os

# client = OpenAI(api_key=os.getenv("OPNEAI_API_KEY"))

# def chat_with_user(db: Session, user_id: int, content: str):
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {"role": "system", "content": "Eres un asistente virtual argentino"},
#             {"role": "user", "content": content}
#         ]
#     )
#     reply = response.choices[0].message.content
#     msg = Message(user_id=user_id, content=content, response=reply)
#     db.add(msg)
#     db.commit()
#     db.refresh(msg)
#     return msg

from fastapi import APIRouter, Depends
from schemas.message import MessageCreate, MessageOut
from services.message import MessageService
from config.database import get_database_session

messages_router = APIRouter()

@messages_router.post('/messages', tags=['Chatbot'], response_model=MessageOut, status_code=201)
def chat(data: MessageCreate,db = Depends(get_database_session),user_id: int = 1  ):
    return MessageService(db).chat_with_user(user_id, data.content)

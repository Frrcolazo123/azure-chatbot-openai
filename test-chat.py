# from email import message
# import os
# from pyexpat.errors import messages
# from openai import OpenAI
# from dotenv import load_dotenv
# from fastapi import FastAPI
# from config.database import Base, engine
# from routers import auth, chat

# Base.metadata.create_all(bind=engine)

# app = FastAPI()
# app.include_router(auth.router)
# app.include_router(chat.router)

# #VARIABLES DE ENTORNO
# load_dotenv()
# api_key_openai = os.getenv("OPNEAI_API_KEY")

# #INSTANCIAR CLIENTE
# client = OpenAI(api_key=api_key_openai)

# #SYSTEM ROLE
# def chat_with_system(system_prompt: str, user_prompt:str ) -> str:
#     """
#     Hace una llamada con system prompt
#     """
#     try:
#         response = client.chat.completions.create(
#             model="gpt-4o-mini", 
#             messages=[
#                 {"role": "system", "content": system_prompt},
#                 {"role": "user", "content": user_prompt}
#             ]
#         )
#         return response.choices[0].message.content
#     except Exception as e:
#         return f"Error: {str(e)}"

# #MEMORIA DEL CHAT
# def chat(prompt:str, message_history: list) -> str:
#     """" 
#     Envía un mensaje y obtinee una respuesta manteniendo el historial
#     """
#     if len(message_history) == 0:
#         system_prompt = "Eres un asistente virtual Argentino"
#         message_history.append({"role": "system", "content": system_prompt})

#     message_history.append({"role": "user", "content": prompt})
#     response = client.chat.completions.create(model="gpt-4o-mini",messages=message_history)
#     assistant_response = response.choices[0].message.content
#     message_history.append({"role": "assistant", "content": assistant_response})

#     return assistant_response


# messages = []
# system_prompt = "Eres un asistente virtual Argentino"
# messages.append({"role": "system", "content": system_prompt})


# #Ejemplo de uso:
# user_prompt = "Cuenta algo argentino"
# respuesta = chat_with_system(system_prompt, user_prompt)
# print(respuesta)

import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get_main_page() -> dict:
    return {'message': 'Главная сираница'}

@app.get('/user/admin')
async def get_admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async  def get_user_page(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user')
async def user_info(username, age) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

from fastapi import FastAPI 
from model.user_connection import UserConnection

app = FastAPI()
conn=UserConnection()

@app.get("/")
def bienvenida():
 return {"message": "Bienvenidos al Blog para hacer operaciones Crud con FastAPI"}



@app.post("/api/insert")
def insert(user_data):
 print(user_data)
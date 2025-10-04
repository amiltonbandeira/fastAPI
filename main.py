from fastapi import FastAPI

app = FastAPI(title="Minha API Básica", version="1.0")

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Olá, {name}!"}

@app.get("/soma")
async def soma(a: int, b: int):
    return {"resultado": a + b}

from fastapi import FastAPI

app = FastAPI()

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to FastAPI!"}

# Route 1: Hello World
@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

# Route 2: Greeting with name
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Route 3: Addition of two numbers
@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

# Route 4: Post request (JSON input)
@app.post("/user/")
def create_user(user: dict):
    return {"message": "User created", "user": user}

# Run using: uvicorn main:app --reload

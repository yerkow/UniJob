from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
def sayHello():
    return {
        "message": 'Hello World'
    }
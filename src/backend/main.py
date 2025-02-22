from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "This is an API to operate with car crashes"}

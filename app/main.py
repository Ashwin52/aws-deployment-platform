from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello from AWS Deployment Platform!", "version":"1.0"}
@app.get("/health")
def health():
    return {"status": "healthy"}

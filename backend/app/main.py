from fastapi import FastAPI

app = FastAPI(
    title="AuraWalk API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "project":"AuraWalk",
        "status":"running"
    }

@app.get("/health")
def health():
    return {
        "status":"ok"
    }
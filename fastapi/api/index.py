from fastapi import FastAPI

# Create a FastAPI app
app = FastAPI()

@app.get("/")

async def health_check():
    return "Hi Hazem Here >> The health check is successful!"


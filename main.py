from fastapi import FastAPI

app = FastAPI()


@app.get("/database")
async def root():
    return {
        "databases": []
    }

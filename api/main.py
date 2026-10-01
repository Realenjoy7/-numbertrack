from fastapi import FastAPI

app = FastAPI()

@app.get("/api/lookup")
def lookup_number(number: str):
    return {
        "status": "success",
        "number": number,
        "message": "Number lookup API is working successfully!"
    }

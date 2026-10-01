from fastapi import FastAPI, HTTPException
import requests

app = FastAPI(title="Phone Number Lookup API")

@app.get("/api/lookup")
def lookup_number(number: str):
    if not number:
        raise HTTPException(status_code=400, detail="Number parameter is missing")

    # Yahan aap apna logic ya kisi external data source/API ka use kar sakte hain
    # Filhal yeh ek sample response de raha hai jo aapke diye gaye format jaisa hai

    # Example logic (Aap yahan real data ya database jod sakte hain)
    response_data = {
        "status": "success",
        "number": number,
        "length": len(number),
        "valid": True,
        "message": "Yeh aapki custom API se generated response hai!"
    }

    return response_data
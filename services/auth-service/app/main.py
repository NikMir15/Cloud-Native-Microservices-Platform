import os
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt

app = FastAPI(title="Auth Service")

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

# Demo in-memory users (we'll replace with DB later)
users = {}

class RegisterRequest(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "auth-service"}

@app.post("/register")
def register(req: RegisterRequest):
    if req.email in users:
        raise HTTPException(status_code=400, detail="User already exists")

    # bcrypt has a 72-byte input limit; reject cleanly
    if len(req.password.encode("utf-8")) > 72:
        raise HTTPException(status_code=400, detail="Password too long (max 72 bytes for bcrypt)")

    try:
        users[req.email] = pwd_context.hash(req.password)
    except Exception as e:
        # Return the real error text (so you can debug) instead of 500 without info
        raise HTTPException(status_code=500, detail=f"Password hashing failed: {type(e).__name__}: {str(e)}")

    return {"message": "registered"}

@app.post("/login")
def login(req: LoginRequest):
    hashed = users.get(req.email)
    if not hashed or not pwd_context.verify(req.password, hashed):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    exp = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = jwt.encode({"sub": req.email, "exp": exp}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

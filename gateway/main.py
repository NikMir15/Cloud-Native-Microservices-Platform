from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://nikmir15.github.io",
        "https://nikmir15.github.io/Cloud-Native-Microservices-Platform"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.config import settings

def register_cors(app: FastAPI):
  """
    跨域
  """
  app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=[str(origin) for origin in settings.CORS_ORIGINS],
    allow_credentials=True,
    allow_methods=("GET", "POST", "PUT", "DELETE", "PATCH"),
    allow_headers=("*", "authentication"),
  )

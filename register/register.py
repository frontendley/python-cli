from fastapi import FastAPI

from register.cors import register_cors
from register.router import register_router


def register(app: FastAPI):
  register_cors(app)
  register_router(app)
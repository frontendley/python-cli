
from fastapi import FastAPI

from register.register import register

def create_app():
  app = FastAPI()
  register(app)
  return app

app = create_app()
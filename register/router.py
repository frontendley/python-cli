from fastapi import FastAPI
from router.feishu import router as feishu_router

def register_router(app: FastAPI):
  app.include_router(feishu_router)
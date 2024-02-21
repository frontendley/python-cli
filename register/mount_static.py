# from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles

# from config.config import settings

# def register_mount_static(app: FastAPI):
#   """
#     挂载静态文件 -- https://fastapi.tiangolo.com/zh/tutorial/static-files/
#   """

#   app.mount(f"/{settings.STATIC_DIR}", StaticFiles(directory=settings.STATIC_DIR), name=settings.STATIC_DIR)
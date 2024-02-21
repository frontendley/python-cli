from typing import List
from pydantic import AnyHttpUrl

class Settings():
  CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]  # 跨域请求


settings = Settings()
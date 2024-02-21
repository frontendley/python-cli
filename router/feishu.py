from fastapi import APIRouter, Request
from service.feishu import handle_feishu_robot
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

router = APIRouter(
  prefix="/feishu_service",
  tags=["feishu-service"]
)

@router.get(
  "/robot_test",
  summary="test ai bot"
)
async def get_receive_bot(request: Request):
  # result = await request.json()
  print(request)
  return {
    "code": "123",
  }

@router.post('/robot_communicate', summary="receive feishu robot communicate")
async def post_receive_communicate(request: Request):
    html_content = """
    <html>
    <head>
        <title>My HTML Page</title>
    </head>
    <body>
        <h1>Hello, world!</h1>
        <p>This is a simple HTML page.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
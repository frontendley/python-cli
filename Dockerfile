# 1、从官方 Python 基础镜像开始
FROM python:3.6.9

# 2、将当前工作目录设置为 /code
# 这是放置 requirements.txt 文件和应用程序目录的地方
WORKDIR /code

# 3、先复制 requirements.txt 文件
# 由于这个文件不经常更改，Docker 会检测它并在这一步使用缓存，也为下一步启用缓存
COPY ./requirements.txt /code/requirements.txt

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=1000 --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/
#CMD ["uvicorn", "main:app", "--ssl-keyfile", "124.222.125.232-key.pem", "--ssl-certfile", "124.222.125.232.pem", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

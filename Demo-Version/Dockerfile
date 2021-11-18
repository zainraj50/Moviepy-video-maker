FROM python:3.8-slim-buster



WORKDIR /app

RUN pip install cx_Oracle flask datetime werkzeug moviepy pandas requests tqdm

COPY . .


CMD [ "python3", "-m" , "file_upload", "--host=0.0.0.0"]

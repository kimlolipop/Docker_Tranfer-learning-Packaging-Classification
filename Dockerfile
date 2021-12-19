FROM python:3.7

COPY . /code

COPY ./requirements.txt /code/requirements.txt

WORKDIR code

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
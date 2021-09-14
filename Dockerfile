FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./webapp /webapp
COPY ./requirements.txt /webapp

WORKDIR /webapp

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
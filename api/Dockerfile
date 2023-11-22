FROM python:3.11

WORKDIR /app

COPY ./api /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 6525

CMD ["python", "/app/app.py"]
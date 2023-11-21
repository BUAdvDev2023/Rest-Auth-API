FROM python:3.11

WORKDIR /app

COPY ./api /app

RUN --no-cache pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 6525

CMD ["python", "/app/app.py"]
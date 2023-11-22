FROM python:3.11

WORKDIR /app

COPY ./api /app

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 6525

CMD ["python", "/app/app.py"]
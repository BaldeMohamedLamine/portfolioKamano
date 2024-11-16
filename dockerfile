FROM python:3.13-slim
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
EXPOSE 8080

CMD 

FROM python:3.12-slim AS builder
WORKDIR /app 
RUN apt-get update 
COPY requirements.txt .
RUN pip install --no-cache --prefix=/install -r requirements.txt

FROM python:3.12-slim 
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 5002
CMD ["python" , "run.py"]

# Stage 1 -Builder-Stage
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2 Runtime-Stage

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .  
EXPOSE 5000
CMD ["python" , "run.py"]

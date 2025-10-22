FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /apps/logs && chmod -R 777 /apps/logs
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
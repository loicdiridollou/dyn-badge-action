FROM python:3
COPY . .
ENTRYPOINT ["python", "test.py"]
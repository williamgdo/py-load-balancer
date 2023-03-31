FROM python:3
RUN pip install flask pymongo
COPY service-b.py /app/app.py
CMD ["python", "/app/app.py"]
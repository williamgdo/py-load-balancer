FROM python:3
RUN pip install flask pymongo
COPY service-a.py /app/app.py
CMD ["python", "/app/app.py"]
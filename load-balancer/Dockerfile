FROM python:3
RUN pip install flask requests
COPY ./load-balancer.py /app/app.py
CMD ["python", "/app/app.py"]
# End-of-life base image, root user, no health check, on purpose
FROM python:3.15
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

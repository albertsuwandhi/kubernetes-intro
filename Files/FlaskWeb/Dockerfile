FROM python:3.7-alpine3.8
COPY . /app
WORKDIR /app
EXPOSE 8080
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "flaskweb.py"]

FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY services/data_loader/ .
EXPOSE 27017
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "27017"]
FROM python:3
WORKDIR /backend
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 7777

CMD ["python", "main.py"]
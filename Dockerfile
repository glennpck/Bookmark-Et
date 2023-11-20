FROM python:3.11.5

WORKDIR /Bookmark-Et

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=run.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
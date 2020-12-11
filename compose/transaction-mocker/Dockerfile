FROM continuumio/anaconda3

ADD ./app /app

RUN pip install -r /app/requirements.txt
CMD ["python", "/app/mocker.py"]

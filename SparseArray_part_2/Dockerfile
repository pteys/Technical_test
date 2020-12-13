FROM python:3.7

WORKDIR /opt/app

ENV SPARSE_ARRAY_STRINGS="ab,ab,abc"

COPY . /opt/app

RUN pip install -r requirements.txt

ENTRYPOINT ["python","main.py"]
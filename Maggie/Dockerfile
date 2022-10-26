FROM python:3.9

RUN mkdir app
RUN mkdir /app/General
RUN mkdir /app/Homer
RUN mkdir /app/Lisa

COPY main.py /app/
COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python","app/main.py"]
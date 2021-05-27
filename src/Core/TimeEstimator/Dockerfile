FROM python:3.9.5-alpine3.13

RUN pip3 install pika

COPY TimeEstimator.py /app/

WORKDIR /app

EXPOSE 5672

ENTRYPOINT ["python3","/app/TimeEstimator.py"]


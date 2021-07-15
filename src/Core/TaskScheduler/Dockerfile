FROM python:3.9.5-alpine3.13

RUN pip3 install pika &&  \
pip3 install -U flatbuffers

COPY MSC_msg /app/MSC_msg

COPY Scheduler.py /app/

WORKDIR /app

EXPOSE 5672

ENTRYPOINT ["python3","/app/Scheduler.py"]


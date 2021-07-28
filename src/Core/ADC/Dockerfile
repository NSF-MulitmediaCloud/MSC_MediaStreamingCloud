FROM python:3.9.5-alpine3.13

RUN pip3 install pika &&  \
pip3 install -U flatbuffers

COPY MSC_msg /app/MSC_msg

COPY ADC.py /app/

WORKDIR /app

EXPOSE 60008

ENTRYPOINT ["python3","/app/ADC.py"]


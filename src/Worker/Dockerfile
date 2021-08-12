FROM jrottenberg/ffmpeg:3.4-ubuntu


RUN apt update && \
apt install -y python3 python3-pip curl gnupg apt-transport-https --no-install-recommends 

RUN curl -1sLf \
  'https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/setup.deb.sh' \
  | bash


RUN pip3 install pika && \
pip3 install -U flatbuffers


#make image small
RUN rm -rf /var/lib/apt/lists/*

WORKDIR /home

COPY Handler.py /home/Handler.py

EXPOSE 5672

ENTRYPOINT ["python3"]
CMD ["/home/Handler.py"]


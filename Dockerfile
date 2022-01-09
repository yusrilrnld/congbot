FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/poocong/PocongUserbot /home/poconguserbot/ \
    && chmod 777 /home/poconguserbot \
    && mkdir /home/poconguserbot/bin/

COPY ./sample_config.env ./config.env* /home/poconguserbot/

WORKDIR /home/poconguserbot/

CMD ["python3", "-m", "userbot"]

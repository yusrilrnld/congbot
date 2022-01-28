FROM mrismanaziz/man-userbot:buster

RUN git clone -b main https://github.com/poocong/PocongUserbot /home/poconguserbot/ \
    && chmod 777 /home/poconguserbot \
    && mkdir /home/poconguserbot/bin/

WORKDIR /home/poconguserbot/

CMD [ "bash", "start" ]
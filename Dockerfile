FROM poocongonlen/poconguserbot:buster

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm

RUN git clone -b main https://github.com/yusrilrnld/congbot /home/congbot/ \
    && chmod 777 /home/congbot \
    && mkdir /home/congbot/bin/

WORKDIR /home/congbot/

CMD [ "bash", "start" ]

FROM python:3.6-alpine 
MAINTAINER BY "Daniel Paes danspaes@gmail.com"

ADD ./twitter_scrapper.py /opt

WORKDIR /opt

RUN python3 -m pip install tweepy

CMD ["python3", "/opt/twitter_scrapper.py"]
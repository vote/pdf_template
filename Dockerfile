FROM python:3.7-buster

ENV APP_DIR=/app
WORKDIR $APP_DIR

RUN apt-get update && \
    apt-get install -y pdftk-java imagemagick ghostscript && \
    apt-get clean

COPY docker/imagemagick-dev-policy.xml /etc/ImageMagick-6/policy.xml

COPY requirements.txt $APP_DIR/
RUN pip install -r requirements.txt

CMD make test_inner

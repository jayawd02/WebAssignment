FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"
WORKDIR /usr/src/app
COPY . .
#COPY ./requirements.txt ./

RUN pip install -r requirements.txt

#COPY . /app

#COPY ./scripts /scripts

RUN chmod +x ./scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

EXPOSE 8000

CMD ["sh","./scripts/docker-entrypoint.sh"]
#CMD ["python","./manage.py","runserver","0.0.0.0:8000"]




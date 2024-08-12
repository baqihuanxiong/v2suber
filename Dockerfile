FROM python:3.10-alpine

WORKDIR /v2suber

COPY ./main.py /v2suber/main.py

EXPOSE 8079

VOLUME /data

CMD ["python", "main.py"]

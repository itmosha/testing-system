FROM python:3.8-alpine
WORKDIR /

COPY requirements.txt .

ENV USER appuser
RUN addgroup -S appgroup && adduser -S $USER -G appgroup
USER $USER

RUN pip3 install -r requirements.txt

USER root

RUN apk update && apk add gcc musl-dev

RUN mkdir uploads && chmod 777 uploads
COPY . .

USER $USER
CMD ["python3", "-u", "main.py"]

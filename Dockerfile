FROM python:3.9-alpine

RUN adduser -D server
WORKDIR /home/server

# Copy requirements first as to not disturb cache for other changes.
COPY requirements.txt .

RUN apk add -U --no-cache libpq

RUN apk add --no-cache --virtual .build-deps build-base postgresql-dev && \
  pip3 install -r requirements.txt && \
  pip3 install gunicorn && \
  apk del .build-deps

USER server

# Finally, copy the entire source.
COPY . .

ENV FLASK_APP room.py
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-b", ":5000", "--access-logfile", "-", "--error-logfile", "-", "main:app"]

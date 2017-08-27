FROM arm32v6/alpine

RUN apk update \
  && apk add --no-cache python3

RUN apk add --no-cache --virtual .build-deps \
		gcc \
		git \
		musl-dev \
		python3-dev

WORKDIR /app
ADD . .

RUN pip3 install --no-cache-dir -Ur requirements.txt \
 && apk del --purge .build-deps

ENTRYPOINT python3 app.py

FROM golang:1.14-alpine AS build-env
RUN apk add --no-cache git make curl sed
WORKDIR /build
RUN git clone https://github.com/oragono/oragono.git .
RUN git submodule update --init
RUN go build

FROM python:alpine
WORKDIR /app
ADD . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY --from=build-env /build/oragono /usr/bin/oragono 
COPY --from=build-env /build/languages languages
COPY --from=build-env /build/oragono.yaml ircd.yaml
RUN sed -i 's/^\s*\"\[::1\]:6667\":.*$//' ircd.yaml
CMD ["/app/entrypoint.sh"]


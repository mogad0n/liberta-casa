FROM golang:1.14-alpine AS build-env
RUN apk add --no-cache git make curl sed
WORKDIR /build
RUN git clone https://github.com/oragono/oragono.git .
RUN git submodule update --init
RUN go build

FROM python:alpine
RUN apk add nginx nodejs yarn git npm
WORKDIR /app
ADD . .
RUN pip3 install -r requirements.txt
RUN git clone https://github.com/kiwiirc/kiwiirc.git /app/kiwi
WORKDIR /app/kiwi
RUN yarn install && yarn build
COPY --from=build-env /build/oragono /usr/bin/oragono 
COPY --from=build-env /build/languages languages
COPY --from=build-env /build/oragono.yaml ircd.yaml
RUN sed -i 's/^\s*\"\[::1\]:6667\":.*$//' ircd.yaml
EXPOSE 80
CMD ["/app/entrypoint.sh"]


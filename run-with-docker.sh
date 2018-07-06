#!/bin/sh

export DOCKER_IMAGE=freekkalter/totd
export CONTAINER=totd

# on host target uncommnet pull and commnet build
# docker pull $DOCKER_IMAGE
docker build --tag $DOCKER_IMAGE .

docker stop $CONTAINER
docker rm $CONTAINER
docker run -it -v $(pwd)/tweets.json:/data/tweets.json \
              -v $(pwd)/instance/flask.cfg:/code/instance/flask.cfg:ro \
              -p 8000:8000 \
              --name $CONTAINER $DOCKER_IMAGE bash


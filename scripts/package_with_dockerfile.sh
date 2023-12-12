#!/usr/bin/env bash

echo "Create package lambda.zip"

docker build . -t aws-lambda

CONTAINER_ID=$(docker create aws-lambda)

mkdir build
docker cp "${CONTAINER_ID}":/tmp/lambda.zip build/lambda.zip
docker rm "${CONTAINER_ID}"

echo "End create package"

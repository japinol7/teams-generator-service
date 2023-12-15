#!/usr/bin/env bash

LAMBDA_RUNTIME=3.11
LAMBDA_PATH=$(pwd)

echo "Create package lambda.zip"

docker run --rm -v "${LAMBDA_PATH}":/var/task --entrypoint //bin/bash amazon/aws-lambda-python:${LAMBDA_RUNTIME} -c "
  if [ '$1' == '--devtest' ] ; then echo 'TEST. --devtest argument detected. Unit tests will be executed as part of this process.' ; fi &&
  set -x &&
  yum install -y zip &&
  pip3.11 install virtualenv &&
  mkdir -p /var/build &&
  zip -R /var/build/lambda.zip '*.py' -x '\.*' 'venv/*' 'tmp/\*' '\*/__pycache__/\*' '\*/.* tests/\*' '\*/tests/\*' &&
  virtualenv /var/lambda &&
  source /var/lambda/bin/activate &&
  if [ '$1' == '--devtest' ] ; then pip3.11 install -r requirements-dev.txt ; else pip3.11 install -r requirements.txt ; fi &&
  if [ '$1' == '--devtest' ] ; then python3.11 -m pytest tests; fi &&
  cd \`python -c 'import sys; print(sys.path[-1])'\` &&
  zip -q -r /var/build/lambda.zip . -x __pycache__/\* \*/__pycache__/\* &&
  mkdir -p /var/task/build &&
  mv /var/build/lambda.zip /var/task/build"

echo "End create package"

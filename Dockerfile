FROM amazon/aws-lambda-python:3.11
LABEL authors="japinol"

RUN yum -y install zip

WORKDIR /lambda

COPY lambda_function.py /lambda
COPY ./modules /lambda/modules

COPY requirements.txt .
RUN  pip3 install -r requirements.txt --target "/lambda"

RUN zip -r /tmp/lambda.zip .

ENTRYPOINT ["python3"]
CMD [ "lambda_function.lambda_handler" ]

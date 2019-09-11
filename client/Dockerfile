FROM gnes/gnes:latest-buster

RUN pip install git+https://github.com/gnes-ai/gnes.git@fix-cli-client --no-cache-dir --compile

ADD *.py ./

ENTRYPOINT ["python", "app.py", "--grpc_port", "5566"]
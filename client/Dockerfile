FROM gnes/gnes:latest-alpine

ADD *.py ./

ENTRYPOINT ["python", "app.py", "--grpc_port", "5566"]
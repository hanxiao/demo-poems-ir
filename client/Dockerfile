FROM gnes/gnes:latest-buster

RUN apt-get update && apt-get install --no-install-recommends -y git

RUN echo 3

RUN pip install -U git+https://github.com/gnes-ai/gnes.git --no-cache-dir --compile

ADD *.py ./

ENTRYPOINT ["python", "app.py", "--grpc_port", "5566"]
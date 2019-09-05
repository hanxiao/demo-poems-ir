FROM continuumio/anaconda3

LABEL maintainer="team@gnes.ai"

RUN apt-get update && apt-get install -y build-essential && \
    /opt/conda/bin/conda install faiss-cpu -c pytorch

ADD *.py *.yml ./

ARG BUILD_TIME

RUN /opt/conda/bin/pip install git+https://github.com/gnes-ai/gnes.git --no-cache-dir --compile

ENTRYPOINT ["/opt/conda/bin/gnes", "index", "--yaml_path", "faiss.yml"]
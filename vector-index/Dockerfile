FROM continuumio/anaconda3

LABEL maintainer="team@gnes.ai"

RUN apt-get update && apt-get install -y build-essential && \
    /opt/conda/bin/conda install faiss-cpu -c pytorch

RUN echo 2
RUN /opt/conda/bin/pip install git+https://github.com/gnes-ai/gnes.git@fix-empty-chunk-inde --no-cache-dir --compile

ADD *.py *.yml ./

ENTRYPOINT ["/opt/conda/bin/gnes", "index", "--yaml_path", "faiss.yml"]
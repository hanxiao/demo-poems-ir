FROM continuumio/anaconda3

LABEL maintainer="team@gnes.ai"

RUN apt-get update && apt-get install -y build-essential && \
    /opt/conda/bin/conda install faiss-cpu -c pytorch

ADD *.py *.yml ./

# placeholder to force rebuild
RUN echo 11

# you can install from PyPi, the following just ensure install latest master
RUN /opt/conda/bin/pip install -U git+https://github.com/gnes-ai/gnes.git --no-cache-dir --compile

ENTRYPOINT ["/opt/conda/bin/gnes", "index", "--yaml_path", "faiss.yml"]
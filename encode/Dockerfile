FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

LABEL maintainer="team@gnes.ai"

RUN pip install pytorch-transformers gnes --no-cache-dir --compile && \
    python -c "from pytorch_transformers import *; x='bert-base-uncased'; BertModel.from_pretrained(x); BertTokenizer.from_pretrained(x)"

ADD *.py *.yml ./
# [Optional] run a simple unit test
# you probably want to comment out this line in the CICD pipeline,
# as your CI runner for "docker build" may not have enough memory
RUN python -m unittest test_transformer.py -v

ENTRYPOINT ["gnes", "encode", "--yaml_path", "transformer.yml", "--read_only"]
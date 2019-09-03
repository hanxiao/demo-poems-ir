FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

LABEL maintainer="team@gnes.ai"

RUN pip install pytorch-transformers --no-cache-dir --compile && \
    python -c "from pytorch_transformers import *; x='bert-base-uncased'; BertModel.from_pretrained(x); BertTokenizer.from_pretrained(x)"

RUN pip install git+https://github.com/gnes-ai/gnes.git --no-cache-dir --compile

ADD *.py *.yml ./

RUN python -m unittest test_transformer.py


ENTRYPOINT ["gnes", "encode", "--yaml_path", "transformer.yml", "--read_only"]
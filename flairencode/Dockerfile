FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

LABEL maintainer="team@gnes.ai"

RUN pip install flair git+https://github.com/gnes-ai/gnes.git --no-cache-dir --compile

## fix unknown SSL problem in Flair
## NOT WORKING, CANT FIX IT FOR NOW
# RUN pip install -U requests[security] pyopenssl
#ENV PYTHONHTTPSVERIFY=0
# EXPOSE 443
# but I'm guessing its Tencent internal network ssl problem, no time to try in other places yet

# trigger the download and store it in the image
RUN python -c "from gnes.encoder.text.flair import FlairEncoder; FlairEncoder().encode(['hello world'])"

ADD *.py *.yml ./

ENTRYPOINT ["gnes", "encode", "--yaml_path", "flair.yml", "--read_only"]
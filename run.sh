#!/usr/bin/env bash

SLEEP_SEC=5

# init swarm env
docker swarm init

set -e

# close the last stack and sleep for a while until it's done
docker stack rm my-gnes && sleep ${SLEEP_SEC}

# build preprocess image
cd preprocess && docker build -t demo-poem-preprocess . && cd -
# build encode image
cd encode && docker build -t demo-poem-encode . && cd -

# deploy the whole stack and sleep for a while until it's done
docker stack deploy --compose-file demo-poem-gnes.yml my-gnes && sleep ${SLEEP_SEC}

# unset proxy as otherwise grpc wont work
unset https_proxy && unset http_proxy && python app.py --mode index --batch_size 4 --grpc_port 5566
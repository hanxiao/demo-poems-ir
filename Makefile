all: clean build deploy
build:
	cd encode && docker build --network=host -t gnes/demo:poem-encode . && cd - && \
	cd preprocess && docker build --network=host -t gnes/demo:poem-preprocess . && cd - && \
	cd vector-index && docker build --network=host -t gnes/demo:poem-vector-index . && cd - && \
	cd fulltext-index && docker build --network=host -t gnes/demo:poem-fulltext-index . && cd -
	cd client && docker build --network=host -t gnes/demo:poem-client . && cd -
push:
	docker push gnes/demo:poem-encode && \
	docker push gnes/demo:poem-preprocess && \
	docker push gnes/demo:poem-vector-index && \
	docker push gnes/demo:poem-fulltext-index && \
	docker push gnes/demo:poem-client
pull:
	docker pull gnes/demo:poem-encode && \
	docker pull gnes/demo:poem-preprocess && \
	docker pull gnes/demo:poem-vector-index && \
	docker pull gnes/demo:poem-fulltext-index && \
	docker pull gnes/demo:poem-client
clean: ; rm -rf .cache && mkdir -p .cache && docker stack rm my-gnes
deploy: ; mkdir -p .cache && docker stack deploy --compose-file demo-poem-index.yml my-gnes
index: ; unset https_proxy && unset http_proxy && docker run --rm --network host -v ${PWD}/data:/data/ gnes/demo:poem-client --mode index --batch_size 4 --txt_file /data/kaggle_poem_dataset.csv
query:
	docker stack rm my-gnes && \
	docker stack deploy --compose-file demo-poem-query.yml my-gnes && \
	unset https_proxy && unset http_proxy && docker run --rm --network host -v ${PWD}/data:/data/ gnes/demo:poem-client --mode query --txt_file /data/kaggle_poem_dataset.csv
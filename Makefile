all: clean build push
build:
	cd encode && docker build --network=host -t gnes/demo-poem:encode . && cd - && \
	cd vector-index && docker build --network=host -t gnes/demo-poem:vector-index . && cd - && \
	cd client && docker build --network=host -t gnes/demo-poem:client . && cd -
push:
	docker push gnes/demo-poem:encode && \
	docker push gnes/demo-poem:vector-index && \
	docker push gnes/demo-poem:client
pull:
	docker pull gnes/gnes:latest-alpine && \
	docker pull gnes/demo-poem:encode && \
	docker pull gnes/demo-poem:vector-index && \
	docker pull gnes/demo-poem:client
clean_data: ; rm -rf .cache && mkdir -p .cache
clean: ; docker stack rm my-gnes
wait: ; @printf "sleep 15s for docker recycling network resources...\n"; sleep 15
deploy_index: ; docker stack deploy --compose-file demo-poem-index.yml my-gnes
deploy_query: ; docker stack deploy --compose-file demo-poem-query.yml my-gnes
client_index: ; unset https_proxy && unset http_proxy && docker run --rm --network host -v ${PWD}/data:/data/ gnes/demo-poem:client --mode index --batch_size 4 --txt_file /data/kaggle_poem_dataset.csv
client_query: ; unset https_proxy && unset http_proxy && docker run -it --rm --network host -v ${PWD}/data:/data/ gnes/demo-poem:client --mode query --txt_file /data/kaggle_poem_dataset.csv
index: clean wait deploy_index
query: clean wait deploy_query
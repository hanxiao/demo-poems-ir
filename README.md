# Semantic Poem Search Demo using GNES

This demo shows you how to build a semantic poem search using GNES. 

## Prerequisite

You need to have [Docker](https://docs.docker.com/install/) installed on your machine.

As a start, run the following command to initialize the Docker Swarm environment.

```bash
docker swarm init
``` 

## 1. Download required GNES images 

```bash
make pull
```

### (Optional) Build images from local

```bash
make build
```

## 2. Index all poems

```bash
make index
# wait for a minute until all services started and grpc is ready
make client_index
```

## 3. Query and show top-10 poems

```bash
make query
# wait for a minute until all services started and grpc is ready
make client_query
```


## Other commands

| Command | Description |
|---|---|
| `make clean` | Clean index files in `.cache` and remove all docker stacks |
| `make clean_stack` | Remove all docker stacks |
| `make clean_data` | Remove all index files in `.cache` |
| `make deploy_query` | Deploy the stack described in `demo-poem-query.yml` for query |
| `make deploy_index` | Deploy the stack described in `demo-poem-index.yml` for index |


## Troubleshooting

If you encounter the following errors when doing `make`, simply wait for couple of seconds. Docker is sometimes slow on recycling network device.

```bash
rm -rf .cache && mkdir .cache && docker stack rm my-gnes
Removing network my-gnes_default
Failed to remove network b0ei205abak98pn84yj9f6u70: Error response from daemon: network b0ei205abak98pn84yj9f6u70 not foundFailed to remove some resources from stack: my-gnes
make: *** [clean] Error 1
```

```bash
Creating service my-gnes_Router40
failed to create service my-gnes_Router40: Error response from daemon: network my-gnes_default not found
make: *** [deploy] Error 1
```

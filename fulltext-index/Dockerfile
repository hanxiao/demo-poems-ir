FROM gnes/gnes:latest-alpine

ADD *.py *.yml ./

ENTRYPOINT ["gnes", "index", "--py_path", "index.py", "--yaml_path", "index.yml"]
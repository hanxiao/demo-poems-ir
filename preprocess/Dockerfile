FROM gnes/gnes:latest-alpine

ADD *.py ./

ENTRYPOINT ["gnes", "preprocess", "--py_path", "split.py", "--yaml_path", "SentSplitPreprocessor"]
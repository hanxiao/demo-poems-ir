FROM gnes/gnes:stable-alpine

ADD poem_preproc.py .

ENTRYPOINT ["gnes", "preprocess", "--py_path", "poem_preproc.py", "--yaml_path", "SentSplitPreprocessor"]
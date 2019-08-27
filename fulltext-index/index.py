from typing import List

from gnes.component import BaseTextIndexer


class SimpleDictIndexer(BaseTextIndexer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._content = {}

    def add(self, keys: List[int], docs: List['gnes_pb2.Document'], *args, **kwargs):
        self._content.update({k: d for (k, d) in zip(keys, docs)})

    def query(self, keys: List[int], *args, **kwargs) -> List['gnes_pb2.Document']:
        return [self._content[k] for k in keys]

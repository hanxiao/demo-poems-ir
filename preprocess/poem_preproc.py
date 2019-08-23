import json
import re

from gnes.component import BaseTextPreprocessor


class SentSplitPreprocessor(BaseTextPreprocessor):
    def __init__(self, max_sent_len: int = 128, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_sent_len = max_sent_len

    def apply(self, doc: 'gnes_pb2.Document') -> None:
        super().apply(doc)
        d = json.loads(doc.raw_bytes.decode())
        doc.raw_text = d.pop('Content')
        doc.meta_info = json.dumps(d).encode()
        for ci, s in enumerate(re.split(r'[.!?]+', doc.raw_text)):
            if s.strip():
                c = doc.chunks.add()
                c.doc_id = doc.doc_id
                c.text = s.strip()[:self.max_sent_len]
                c.offset_1d = ci
                c.weight = len(c.text) / len(doc.raw_text)

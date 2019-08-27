import json
import re
import string

from gnes.component import BaseTextPreprocessor


class SentSplitPreprocessor(BaseTextPreprocessor):
    def __init__(self, max_sent_len: int = 256, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_sent_len = max_sent_len

    def apply(self, doc: 'gnes_pb2.Document') -> None:
        super().apply(doc)
        d = json.loads(doc.raw_bytes.decode())
        doc.raw_text = d.pop('Content')
        doc.meta_info = json.dumps(d).encode()

        ret = [(m.group(0), m.start(), m.end()) for m in re.finditer(r'[^.!?]+[.!?]', doc.raw_text)]
        for ci, (r, s, e) in enumerate(ret):
            f = ''.join(filter(lambda x: x in string.printable, r))
            f = re.sub('\n+', ' ', f).strip()
            if f:
                c = doc.chunks.add()
                c.doc_id = doc.doc_id
                c.text = f[:self.max_sent_len]
                c.offset_1d = ci
                c.weight = len(c.text) / len(doc.raw_text)
                c.offset_nd.x.extend([s, e])

import csv
import json
from typing import List

from gnes.cli.parser import set_client_cli_parser
from gnes.client.cli import ProgressBar, CLIClient
from gnes.proto import RequestGenerator
from termcolor import colored


class MyClient(CLIClient):
    def read_all(self):
        return [json.dumps(rr).encode() for rr in csv.DictReader(self.args.txt_file, delimiter=',', quotechar='"')][
               :100]

    def index(self, all_bytes: List[bytes], stub):
        with ProgressBar(all_bytes, self.args.batch_size, task_name='index') as p_bar:
            for _ in stub.StreamCall(RequestGenerator.index(all_bytes,
                                                            random_doc_id=False,
                                                            batch_size=self.args.batch_size)):
                p_bar.update()

    def query(self, all_bytes: List[bytes], stub):
        for idx, q in enumerate(all_bytes):
            for req in RequestGenerator.query(q, request_id_start=idx, top_k=self.args.top_k):
                resp = stub.Call(req)
                print(colored(req.search.query, 'green'))
                for k in resp.search.topk_results:
                    print(colored(k.doc.doc_id, 'magenta'))
                    print(colored(k.doc.raw_text, 'yellow'))
                    print(colored(k.score, 'blue'))
                    print(colored(k.score_explained, 'cyan'))
                    input('press any key to continue...')
                input('on to next query, press any key to continue...')


if __name__ == '__main__':
    MyClient(set_client_cli_parser().parse_args())

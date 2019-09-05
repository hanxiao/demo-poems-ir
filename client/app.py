import csv
import json
import pprint
from typing import List

from gnes.cli.parser import set_client_cli_parser
from gnes.client.cli import CLIClient
from gnes.proto import RequestGenerator
from termcolor import colored


class MyClient(CLIClient):
    def read_all(self):
        return [json.dumps(rr).encode() for rr in csv.DictReader(self.args.txt_file, delimiter=',', quotechar='"')][
               :10]

    def query(self, all_bytes: List[bytes], stub):
        for idx, q in enumerate(all_bytes):
            for req in RequestGenerator.query(q, request_id_start=idx, top_k=self.args.top_k):
                resp = stub.Call(req)
                print(colored(req.search.query, 'green'))
                for k in resp.search.topk_results:
                    print(colored(k.doc.doc_id, 'magenta'))
                    print(colored(k.doc.raw_text, 'yellow'))
                    print(colored(k.score.value, 'blue'))
                    pprint.pprint(json.loads(k.score.explained))
                    input('press any key to continue...')
                input('on to next query, press any key to continue...')


if __name__ == '__main__':
    MyClient(set_client_cli_parser().parse_args())

import csv
import json
from typing import List

from gnes.cli.parser import set_client_cli_parser
from gnes.client.cli import ProgressBar, CLIClient
from gnes.proto import RequestGenerator


class MyClient(CLIClient):
    def read_all(self):
        with open('data/kaggle_poem_dataset.csv', encoding='utf8') as csvfile:
            return [json.dumps(rr).encode() for rr in csv.DictReader(csvfile, delimiter=',', quotechar='"')][:100]

    def index(self, all_bytes: List[bytes], stub):
        with ProgressBar(all_bytes, self.args.batch_size, task_name='index') as p_bar:
            for _ in stub.StreamCall(RequestGenerator.index(all_bytes,
                                                            random_doc_id=False,
                                                            batch_size=self.args.batch_size)):
                p_bar.update()


if __name__ == '__main__':
    MyClient(set_client_cli_parser().parse_args())

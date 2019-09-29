import csv
import json
import pprint

from gnes.cli.parser import set_client_cli_parser
from gnes.client.cli import CLIClient
from termcolor import colored


class MyClient(CLIClient):

    @property
    def bytes_generator(self):
        num_rows = 0
        for rr in csv.DictReader(self.args.txt_file, delimiter=',', quotechar='"'):
            yield json.dumps(rr).encode()
            num_rows += 1
            if num_rows > self.args.num_poems:
                return

    def query_callback(self, req, resp):
        print(colored(req.search.query, 'green'))
        for k in resp.search.topk_results:
            print(colored(k.doc.doc_id, 'magenta'))
            print(colored(k.doc.raw_text, 'yellow'))
            print(colored(k.score.value, 'blue'))
            pprint.pprint(json.loads(k.score.explained))
            input('press any key to continue...')
        input('on to next query, press any key to continue...')


if __name__ == '__main__':
    parser = set_client_cli_parser()
    parser.add_argument('--num_poems', type=int,
                        default=10,
                        help='number of poems to index')
    MyClient(parser.parse_args())

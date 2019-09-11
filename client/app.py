import csv
import json
import pprint

from gnes.cli.parser import set_client_cli_parser
from gnes.client.cli import CLIClient
from termcolor import colored


class MyClient(CLIClient):
    def read_all(self):
        return [json.dumps(rr).encode() for rr in csv.DictReader(self.args.txt_file, delimiter=',', quotechar='"')][
               :self.args.num_poems]

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

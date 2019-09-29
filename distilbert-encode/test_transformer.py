import unittest

import grpc
from gnes.cli.parser import set_frontend_parser, set_encoder_parser, set_preprocessor_parser
from gnes.proto import gnes_pb2_grpc, RequestGenerator
from gnes.service.base import ServiceManager, SocketType
from gnes.service.encoder import EncoderService
from gnes.service.frontend import FrontendService
from gnes.service.preprocessor import PreprocessorService


class TestEncoder(unittest.TestCase):

    def test_pymode(self):
        args = set_frontend_parser().parse_args([])

        p_args = set_preprocessor_parser().parse_args([
            '--port_in', str(args.port_out),
            '--port_out', '5531',
            '--socket_in', str(SocketType.PULL_CONNECT),
            '--socket_out', str(SocketType.PUSH_BIND),
            '--yaml_path', 'SentSplitPreprocessor'
        ])

        e_args = set_encoder_parser().parse_args([
            '--port_in', str(p_args.port_out),
            '--port_out', str(args.port_in),
            '--socket_in', str(SocketType.PULL_CONNECT),
            '--socket_out', str(SocketType.PUSH_CONNECT),
            '--yaml_path', 'transformer.yml',
            '--py_path', 'distilbert.py'
        ])

        with ServiceManager(EncoderService, e_args), \
             ServiceManager(PreprocessorService, p_args), \
             FrontendService(args), \
             grpc.insecure_channel('%s:%s' % (args.grpc_host, args.grpc_port),
                                   options=[('grpc.max_send_message_length', 70 * 1024 * 1024),
                                            ('grpc.max_receive_message_length', 70 * 1024 * 1024)]) as channel:
            stub = gnes_pb2_grpc.GnesRPCStub(channel)
            resp = stub.Call(list(RequestGenerator.index([b'hello world, good to see you.', b'goodbye! wish to see you again!'], 1))[0])
            self.assertEqual(resp.request_id, 0)

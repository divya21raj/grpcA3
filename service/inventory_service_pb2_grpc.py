# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import book_pb2 as book__pb2
import inventory_service_pb2 as inventory__service__pb2


class CreateBookStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateBook = channel.unary_unary(
                '/CreateBook/CreateBook',
                request_serializer=inventory__service__pb2.CreateBookRequest.SerializeToString,
                response_deserializer=inventory__service__pb2.CreateBookResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/CreateBook/GetBook',
                request_serializer=inventory__service__pb2.GetBookRequest.SerializeToString,
                response_deserializer=book__pb2.Book.FromString,
                )


class CreateBookServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CreateBookServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateBook': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBook,
                    request_deserializer=inventory__service__pb2.CreateBookRequest.FromString,
                    response_serializer=inventory__service__pb2.CreateBookResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=inventory__service__pb2.GetBookRequest.FromString,
                    response_serializer=book__pb2.Book.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'CreateBook', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CreateBook(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CreateBook/CreateBook',
            inventory__service__pb2.CreateBookRequest.SerializeToString,
            inventory__service__pb2.CreateBookResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/CreateBook/GetBook',
            inventory__service__pb2.GetBookRequest.SerializeToString,
            book__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

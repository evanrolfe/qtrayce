# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import api_pb2 as api__pb2


class TrayceAgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendFlowsObserved = channel.unary_unary(
                '/api.TrayceAgent/SendFlowsObserved',
                request_serializer=api__pb2.Flows.SerializeToString,
                response_deserializer=api__pb2.Reply.FromString,
                )
        self.SendAgentStarted = channel.unary_unary(
                '/api.TrayceAgent/SendAgentStarted',
                request_serializer=api__pb2.AgentStarted.SerializeToString,
                response_deserializer=api__pb2.Reply.FromString,
                )
        self.OpenCommandStream = channel.stream_stream(
                '/api.TrayceAgent/OpenCommandStream',
                request_serializer=api__pb2.NooP.SerializeToString,
                response_deserializer=api__pb2.Command.FromString,
                )


class TrayceAgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendFlowsObserved(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendAgentStarted(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenCommandStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TrayceAgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendFlowsObserved': grpc.unary_unary_rpc_method_handler(
                    servicer.SendFlowsObserved,
                    request_deserializer=api__pb2.Flows.FromString,
                    response_serializer=api__pb2.Reply.SerializeToString,
            ),
            'SendAgentStarted': grpc.unary_unary_rpc_method_handler(
                    servicer.SendAgentStarted,
                    request_deserializer=api__pb2.AgentStarted.FromString,
                    response_serializer=api__pb2.Reply.SerializeToString,
            ),
            'OpenCommandStream': grpc.stream_stream_rpc_method_handler(
                    servicer.OpenCommandStream,
                    request_deserializer=api__pb2.NooP.FromString,
                    response_serializer=api__pb2.Command.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'api.TrayceAgent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TrayceAgent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendFlowsObserved(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.TrayceAgent/SendFlowsObserved',
            api__pb2.Flows.SerializeToString,
            api__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendAgentStarted(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/api.TrayceAgent/SendAgentStarted',
            api__pb2.AgentStarted.SerializeToString,
            api__pb2.Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenCommandStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/api.TrayceAgent/OpenCommandStream',
            api__pb2.NooP.SerializeToString,
            api__pb2.Command.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

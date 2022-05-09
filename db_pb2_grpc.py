# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import db_pb2 as db__pb2


class DatabaseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBox = channel.unary_unary(
                '/DatabaseService/GetBox',
                request_serializer=db__pb2.GetBoxRequest.SerializeToString,
                response_deserializer=db__pb2.GetBoxResponse.FromString,
                )
        self.GetBoxes = channel.unary_unary(
                '/DatabaseService/GetBoxes',
                request_serializer=db__pb2.GetAllBoxesRequest.SerializeToString,
                response_deserializer=db__pb2.GetBoxesResponse.FromString,
                )
        self.CreateBox = channel.unary_unary(
                '/DatabaseService/CreateBox',
                request_serializer=db__pb2.CreateBoxRequest.SerializeToString,
                response_deserializer=db__pb2.CreateBoxResponse.FromString,
                )
        self.UpdateBox = channel.unary_unary(
                '/DatabaseService/UpdateBox',
                request_serializer=db__pb2.UpdateBoxRequest.SerializeToString,
                response_deserializer=db__pb2.UpdateBoxResponse.FromString,
                )
        self.DeleteBox = channel.unary_unary(
                '/DatabaseService/DeleteBox',
                request_serializer=db__pb2.DeleteBoxRequest.SerializeToString,
                response_deserializer=db__pb2.DeleteBoxResponse.FromString,
                )
        self.GetBoxesInCategory = channel.unary_unary(
                '/DatabaseService/GetBoxesInCategory',
                request_serializer=db__pb2.GetBoxesInCategoryRequest.SerializeToString,
                response_deserializer=db__pb2.GetBoxesResponse.FromString,
                )
        self.GetBoxesInTimeRange = channel.unary_unary(
                '/DatabaseService/GetBoxesInTimeRange',
                request_serializer=db__pb2.GetBoxesInTimeRangeRequest.SerializeToString,
                response_deserializer=db__pb2.GetBoxesResponse.FromString,
                )


class DatabaseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBoxes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBoxesInCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBoxesInTimeRange(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatabaseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBox': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBox,
                    request_deserializer=db__pb2.GetBoxRequest.FromString,
                    response_serializer=db__pb2.GetBoxResponse.SerializeToString,
            ),
            'GetBoxes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBoxes,
                    request_deserializer=db__pb2.GetAllBoxesRequest.FromString,
                    response_serializer=db__pb2.GetBoxesResponse.SerializeToString,
            ),
            'CreateBox': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBox,
                    request_deserializer=db__pb2.CreateBoxRequest.FromString,
                    response_serializer=db__pb2.CreateBoxResponse.SerializeToString,
            ),
            'UpdateBox': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateBox,
                    request_deserializer=db__pb2.UpdateBoxRequest.FromString,
                    response_serializer=db__pb2.UpdateBoxResponse.SerializeToString,
            ),
            'DeleteBox': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBox,
                    request_deserializer=db__pb2.DeleteBoxRequest.FromString,
                    response_serializer=db__pb2.DeleteBoxResponse.SerializeToString,
            ),
            'GetBoxesInCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBoxesInCategory,
                    request_deserializer=db__pb2.GetBoxesInCategoryRequest.FromString,
                    response_serializer=db__pb2.GetBoxesResponse.SerializeToString,
            ),
            'GetBoxesInTimeRange': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBoxesInTimeRange,
                    request_deserializer=db__pb2.GetBoxesInTimeRangeRequest.FromString,
                    response_serializer=db__pb2.GetBoxesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DatabaseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatabaseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/GetBox',
            db__pb2.GetBoxRequest.SerializeToString,
            db__pb2.GetBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBoxes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/GetBoxes',
            db__pb2.GetAllBoxesRequest.SerializeToString,
            db__pb2.GetBoxesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/CreateBox',
            db__pb2.CreateBoxRequest.SerializeToString,
            db__pb2.CreateBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/UpdateBox',
            db__pb2.UpdateBoxRequest.SerializeToString,
            db__pb2.UpdateBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/DeleteBox',
            db__pb2.DeleteBoxRequest.SerializeToString,
            db__pb2.DeleteBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBoxesInCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/GetBoxesInCategory',
            db__pb2.GetBoxesInCategoryRequest.SerializeToString,
            db__pb2.GetBoxesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBoxesInTimeRange(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DatabaseService/GetBoxesInTimeRange',
            db__pb2.GetBoxesInTimeRangeRequest.SerializeToString,
            db__pb2.GetBoxesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

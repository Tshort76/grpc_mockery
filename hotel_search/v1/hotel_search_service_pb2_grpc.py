# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from hotel_search.v1 import hotel_search_request_pb2 as hotel__search_dot_v1_dot_hotel__search__request__pb2
from hotel_search.v1 import hotel_search_response_pb2 as hotel__search_dot_v1_dot_hotel__search__response__pb2

GRPC_GENERATED_VERSION = '1.64.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in hotel_search/v1/hotel_search_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class HotelSearchServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HotelSearch = channel.unary_unary(
                '/hotel_search.v1.HotelSearchService/HotelSearch',
                request_serializer=hotel__search_dot_v1_dot_hotel__search__request__pb2.HotelSearchRequest.SerializeToString,
                response_deserializer=hotel__search_dot_v1_dot_hotel__search__response__pb2.HotelSearchResponse.FromString,
                _registered_method=True)


class HotelSearchServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HotelSearch(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HotelSearchServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HotelSearch': grpc.unary_unary_rpc_method_handler(
                    servicer.HotelSearch,
                    request_deserializer=hotel__search_dot_v1_dot_hotel__search__request__pb2.HotelSearchRequest.FromString,
                    response_serializer=hotel__search_dot_v1_dot_hotel__search__response__pb2.HotelSearchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hotel_search.v1.HotelSearchService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('hotel_search.v1.HotelSearchService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class HotelSearchService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HotelSearch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/hotel_search.v1.HotelSearchService/HotelSearch',
            hotel__search_dot_v1_dot_hotel__search__request__pb2.HotelSearchRequest.SerializeToString,
            hotel__search_dot_v1_dot_hotel__search__response__pb2.HotelSearchResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

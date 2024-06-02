import sys
from concurrent import futures

import grpc
import randomproto
from google.protobuf.json_format import MessageToDict, ParseDict

import hotel_search.v1.hotel_search_service_pb2_grpc as hs_grpc
from hotel_search.v1.hotel_search_request_pb2 import HotelSearchRequest
from hotel_search.v1.hotel_search_response_pb2 import HotelSearchResponse
import hotel_search.utils as u


class HotelSearchServicer(hs_grpc.HotelSearchServiceServicer):

    def HotelSearch(self, request: HotelSearchRequest, context={}) -> HotelSearchResponse:
        req = MessageToDict(request, preserving_proto_field_name=True)
        lookup_key = u.mock_lookup_key(req)

        print(f"Checking for mock response associate with key: {lookup_key}")

        if mock_example := u.MOCK_DATA.get(lookup_key):
            if set(mock_example["request"]["property_ids"]) == set(req["property_ids"]):
                print("SERVING MOCK RESPONSE")
                return ParseDict(mock_example.get("response"), HotelSearchResponse())

        print("SERVING RANDOM DATA")
        return randomproto.randproto(HotelSearchResponse)


def serve(server_address: str):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    hs_grpc.add_HotelSearchServiceServicer_to_server(HotelSearchServicer(), server)
    server.add_insecure_port(server_address)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    port = sys.argv[1] if len(sys.argv) > 1 else "50051"
    server_address = f"localhost:{port}"
    print(f"Running insecure server on {server_address}")
    serve(server_address)


# python -m hotel_search.server

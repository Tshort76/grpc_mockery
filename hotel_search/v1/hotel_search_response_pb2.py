# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hotel_search/v1/hotel_search_response.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
from google.type import money_pb2 as google_dot_type_dot_money__pb2
from hotel_search.v1 import common_pb2 as hotel__search_dot_v1_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+hotel_search/v1/hotel_search_response.proto\x12\x0fhotel_search.v1\x1a\x18google/type/latlng.proto\x1a\x17google/type/money.proto\x1a\x1chotel_search/v1/common.proto\"\x9d\x01\n\x13HotelSearchResponse\x12\x30\n\x0bstatus_code\x18\x01 \x01(\x0e\x32\x1b.hotel_search.v1.StatusCode\x12\x1b\n\x0estatus_message\x18\x02 \x01(\tH\x00\x88\x01\x01\x12$\n\x05rooms\x18\x03 \x03(\x0b\x32\x15.hotel_search.v1.RoomB\x11\n\x0f_status_message\"\xfd\x01\n\x04Room\x12\x0f\n\x07room_id\x18\x01 \x01(\x03\x12\x15\n\rmax_occupancy\x18\x02 \x01(\r\x12(\n\x0cnightly_rate\x18\x03 \x01(\x0b\x32\x12.google.type.Money\x12%\n\x05hotel\x18\x04 \x01(\x0b\x32\x16.hotel_search.v1.Hotel\x12\"\n\x04\x62\x65\x64s\x18\x05 \x03(\x0e\x32\x14.hotel_search.v1.Bed\x12+\n\tamenities\x18\x06 \x03(\x0e\x32\x18.hotel_search.v1.Amenity\x12+\n\x08\x63\x61tegory\x18\x07 \x01(\x0e\x32\x19.hotel_search.v1.Category\"e\n\x05Hotel\x12\n\n\x02id\x18\x01 \x01(\x03\x12%\n\x08location\x18\x02 \x01(\x0b\x32\x13.google.type.LatLng\x12\x14\n\x0c\x64isplay_name\x18\x03 \x01(\t\x12\x13\n\x0bstar_rating\x18\x04 \x01(\r*;\n\nStatusCode\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0e\n\nUSER_ERROR\x10\x01\x12\x10\n\x0cSERVER_ERROR\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hotel_search.v1.hotel_search_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STATUSCODE']._serialized_start=664
  _globals['_STATUSCODE']._serialized_end=723
  _globals['_HOTELSEARCHRESPONSE']._serialized_start=146
  _globals['_HOTELSEARCHRESPONSE']._serialized_end=303
  _globals['_ROOM']._serialized_start=306
  _globals['_ROOM']._serialized_end=559
  _globals['_HOTEL']._serialized_start=561
  _globals['_HOTEL']._serialized_end=662
# @@protoc_insertion_point(module_scope)

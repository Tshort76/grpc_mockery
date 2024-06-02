from google.type import latlng_pb2 as _latlng_pb2
from google.type import money_pb2 as _money_pb2
from hotel_search.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SUCCESS: _ClassVar[StatusCode]
    USER_ERROR: _ClassVar[StatusCode]
    SERVER_ERROR: _ClassVar[StatusCode]
SUCCESS: StatusCode
USER_ERROR: StatusCode
SERVER_ERROR: StatusCode

class HotelSearchResponse(_message.Message):
    __slots__ = ("status_code", "status_message", "rooms")
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ROOMS_FIELD_NUMBER: _ClassVar[int]
    status_code: StatusCode
    status_message: str
    rooms: _containers.RepeatedCompositeFieldContainer[Room]
    def __init__(self, status_code: _Optional[_Union[StatusCode, str]] = ..., status_message: _Optional[str] = ..., rooms: _Optional[_Iterable[_Union[Room, _Mapping]]] = ...) -> None: ...

class Room(_message.Message):
    __slots__ = ("room_id", "max_occupancy", "nightly_rate", "hotel", "beds", "amenities", "category")
    ROOM_ID_FIELD_NUMBER: _ClassVar[int]
    MAX_OCCUPANCY_FIELD_NUMBER: _ClassVar[int]
    NIGHTLY_RATE_FIELD_NUMBER: _ClassVar[int]
    HOTEL_FIELD_NUMBER: _ClassVar[int]
    BEDS_FIELD_NUMBER: _ClassVar[int]
    AMENITIES_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    room_id: int
    max_occupancy: int
    nightly_rate: _money_pb2.Money
    hotel: Hotel
    beds: _containers.RepeatedScalarFieldContainer[_common_pb2.Bed]
    amenities: _containers.RepeatedScalarFieldContainer[_common_pb2.Amenity]
    category: _common_pb2.Category
    def __init__(self, room_id: _Optional[int] = ..., max_occupancy: _Optional[int] = ..., nightly_rate: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., hotel: _Optional[_Union[Hotel, _Mapping]] = ..., beds: _Optional[_Iterable[_Union[_common_pb2.Bed, str]]] = ..., amenities: _Optional[_Iterable[_Union[_common_pb2.Amenity, str]]] = ..., category: _Optional[_Union[_common_pb2.Category, str]] = ...) -> None: ...

class Hotel(_message.Message):
    __slots__ = ("id", "location", "display_name", "star_rating")
    ID_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STAR_RATING_FIELD_NUMBER: _ClassVar[int]
    id: int
    location: _latlng_pb2.LatLng
    display_name: str
    star_rating: int
    def __init__(self, id: _Optional[int] = ..., location: _Optional[_Union[_latlng_pb2.LatLng, _Mapping]] = ..., display_name: _Optional[str] = ..., star_rating: _Optional[int] = ...) -> None: ...

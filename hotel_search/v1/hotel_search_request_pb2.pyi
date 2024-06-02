from google.type import date_pb2 as _date_pb2
from google.type import money_pb2 as _money_pb2
from hotel_search.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Device(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MOBILE_APP: _ClassVar[Device]
    MOBILE_BROWSER: _ClassVar[Device]
    DESKTOP_BROWSER: _ClassVar[Device]
MOBILE_APP: Device
MOBILE_BROWSER: Device
DESKTOP_BROWSER: Device

class HotelSearchRequest(_message.Message):
    __slots__ = ("user_session", "guest_count", "check_in_date", "check_out_date", "city_of_interest", "max_nightly_price", "categories", "amenities", "search_radius_km", "beds")
    USER_SESSION_FIELD_NUMBER: _ClassVar[int]
    GUEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHECK_IN_DATE_FIELD_NUMBER: _ClassVar[int]
    CHECK_OUT_DATE_FIELD_NUMBER: _ClassVar[int]
    CITY_OF_INTEREST_FIELD_NUMBER: _ClassVar[int]
    MAX_NIGHTLY_PRICE_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    AMENITIES_FIELD_NUMBER: _ClassVar[int]
    SEARCH_RADIUS_KM_FIELD_NUMBER: _ClassVar[int]
    BEDS_FIELD_NUMBER: _ClassVar[int]
    user_session: UserSession
    guest_count: int
    check_in_date: _date_pb2.Date
    check_out_date: _date_pb2.Date
    city_of_interest: str
    max_nightly_price: _money_pb2.Money
    categories: _containers.RepeatedScalarFieldContainer[_common_pb2.Category]
    amenities: _containers.RepeatedScalarFieldContainer[_common_pb2.Amenity]
    search_radius_km: int
    beds: _containers.RepeatedScalarFieldContainer[_common_pb2.Bed]
    def __init__(self, user_session: _Optional[_Union[UserSession, _Mapping]] = ..., guest_count: _Optional[int] = ..., check_in_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., check_out_date: _Optional[_Union[_date_pb2.Date, _Mapping]] = ..., city_of_interest: _Optional[str] = ..., max_nightly_price: _Optional[_Union[_money_pb2.Money, _Mapping]] = ..., categories: _Optional[_Iterable[_Union[_common_pb2.Category, str]]] = ..., amenities: _Optional[_Iterable[_Union[_common_pb2.Amenity, str]]] = ..., search_radius_km: _Optional[int] = ..., beds: _Optional[_Iterable[_Union[_common_pb2.Bed, str]]] = ...) -> None: ...

class UserSession(_message.Message):
    __slots__ = ("session_id", "user_device", "member_id")
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    USER_DEVICE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    session_id: str
    user_device: Device
    member_id: str
    def __init__(self, session_id: _Optional[str] = ..., user_device: _Optional[_Union[Device, str]] = ..., member_id: _Optional[str] = ...) -> None: ...

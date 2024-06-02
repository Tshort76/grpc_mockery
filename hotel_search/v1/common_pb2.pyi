from google.type import phone_number_pb2 as _phone_number_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Amenity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREE_BREAKFAST: _ClassVar[Amenity]
    WATER_VIEW: _ClassVar[Amenity]
    FREE_PARKING: _ClassVar[Amenity]
    FREE_CANCELLATION: _ClassVar[Amenity]

class Bed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TWIN: _ClassVar[Bed]
    TRUNDLE: _ClassVar[Bed]
    FUTON: _ClassVar[Bed]
    QUEEN: _ClassVar[Bed]
    KING: _ClassVar[Bed]

class Category(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BUDGET: _ClassVar[Category]
    STANDARD: _ClassVar[Category]
    BUSINESS: _ClassVar[Category]
    EXECUTIVE: _ClassVar[Category]
FREE_BREAKFAST: Amenity
WATER_VIEW: Amenity
FREE_PARKING: Amenity
FREE_CANCELLATION: Amenity
TWIN: Bed
TRUNDLE: Bed
FUTON: Bed
QUEEN: Bed
KING: Bed
BUDGET: Category
STANDARD: Category
BUSINESS: Category
EXECUTIVE: Category

class Guest(_message.Message):
    __slots__ = ("name", "email", "country_code", "phone_number", "member_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MEMBER_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    email: str
    country_code: str
    phone_number: _phone_number_pb2.PhoneNumber
    member_id: int
    def __init__(self, name: _Optional[str] = ..., email: _Optional[str] = ..., country_code: _Optional[str] = ..., phone_number: _Optional[_Union[_phone_number_pb2.PhoneNumber, _Mapping]] = ..., member_id: _Optional[int] = ...) -> None: ...

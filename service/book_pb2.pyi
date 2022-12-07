from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FICTION: Genre
NON_FICTION: Genre
SCIENCE: Genre
UNKNOWN: Genre

class Author(_message.Message):
    __slots__ = ["birth_year", "first_name", "last_name"]
    BIRTH_YEAR_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    birth_year: int
    first_name: str
    last_name: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., birth_year: _Optional[int] = ...) -> None: ...

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "published_year", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHED_YEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: Author
    genre: Genre
    isbn: str
    published_year: int
    title: str
    def __init__(self, isbn: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[_Union[Author, _Mapping]] = ..., genre: _Optional[_Union[Genre, str]] = ..., published_year: _Optional[int] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

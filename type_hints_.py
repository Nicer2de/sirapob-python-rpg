from __future__ import annotations

from collections import namedtuple
from dataclasses import dataclass
from typing import (
    Dict,
    Generic,
    List,
    TypeVar,
    Union,
)

Point = namedtuple("Point", ["x", "y"])

point2d = Point(1, 2)
point2d.x
point2d.y


bob: Student

TFriend = TypeVar("TFriend")


@dataclass
class Student(Generic[TFriend]):
    name: str
    age: int
    position: Point
    friends: List[TFriend]


student_that_only_likes_animals: Student[int]

student = Student(
    **{  # type: ignore
        "name": "Marcy",
        "age": 25,
        "position": Point(1, 2),
        "friends": [
            Student(
                **{  # type: ignore
                    "name": "Jared",
                    "age": 25,
                    "position": Point(1, 2),
                    "friends": [],
                }
            )
        ],
    }
)

print(student)

TStudentArgsDictKeys = Union[str, int, Point, List[Student]]
TStudentArgsDict = Dict[str, TStudentArgsDictKeys]

# TAddableEntity = Union[int, float, str, list, tuple]
TAddableEntity = TypeVar("TAddableEntity", int, float, str, list, tuple)
TException = TypeVar("TException", bound=Exception)


def raise_exception(err: TException):
    raise err


raise_exception(ValueError("I'm a value error"))


def make_list_of_addable_entity(
    a: TAddableEntity,
    b: TAddableEntity,
) -> List[TAddableEntity]:
    return [a, b]


def add(a: TAddableEntity, b: TAddableEntity) -> TAddableEntity:
    return a + b


make_list_of_addable_entity(a=1, b=2)[0]

add(a="ba", b="nana")

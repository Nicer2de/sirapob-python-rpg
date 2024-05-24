from dataclasses import dataclass


@dataclass
class Duck:

    def __getattr__(self, attr: str):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swim":
            return lambda: print("splash")
        else:
            raise AttributeError


e = 1

from pathlib import Path
from typing import Type

# var: int = 1
# var = "hi"


# def consume_many_types(
#     num: int,
#     decimal: float,
#     boolean: bool,
#     string: str,
#     binary: bytes,
#     obj: object,
# ) -> None: ...


# from dataclasses import dataclass
# from typing import (
#     Any,
#     Iterable,
#     List,
#     Literal,
#     Mapping,
#     Optional,
#     Sequence,
#     Set,
#     Tuple,
#     Type,
#     Union,
# )

# nums: List[int] = [1, 2, 3, 4]

# three_dimentional_vector: tuple[int, float, str] = (1, 2.0, "hi")
# three_dimentional_vector[0].is_integer

# n_dimensional_vectpr: Tuple[float, ...] = 1, 2, 3, 4, 5
# students_to_ages: Mapping[str, int] = {
#     "bobby": 25,
#     "murph": 27,
#     "alice": 21,
# }
# fruits: Set[str] = {"apple", "kiwi", "banana"}

# miscelllaneous_values: List[Union[int, float, str, Type]] = [1, 1.0, "hi", object]
# x: Union[int, float, str, Type]


# def greet(name: Optional[str] = None):
#     if not name:
#         print("Hello!")
#         return
#     print(f"Hello, {name}!")


# greet(None)

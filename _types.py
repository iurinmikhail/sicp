

from typing import Callable
from enum import Enum, auto

class TypeSelectorEnum(int, Enum):
    """Типы для селектора."""
    NUMER=auto()
    DENOM=auto()

type Index = int
type Numer = int
type Denom = int
Pair = Callable[[TypeSelectorEnum], Numer | Denom]
type DenomEnd = Pair | None
ListPair = Callable[[TypeSelectorEnum], Numer | Pair | DenomEnd]

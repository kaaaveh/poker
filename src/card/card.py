from dataclasses import dataclass

from ..rank.rank import Rank
from ..suit.suit import Suit


@dataclass(frozen=True, slots=True)
class Card:
    """
    Immutable int-backed playing card.

    Internal encoding:
        id = suit * 13 + rank
        id ∈ [0, 51]
    """
    _id: int

    def __post_init__(self):
        if not 0 <= self._id < 52:
            raise ValueError(f"Invalid card ID: {self._id}")
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def rank(self) -> Rank:
        return Rank(self._id % 13)
    
    @property
    def suit(self) -> Suit:
        return Suit(self._id // 13)

    @classmethod
    def of(cls, rank: Rank, suit: Suit) -> "Card":
        return cls(int(suit) * 13 + int(rank))
    
    
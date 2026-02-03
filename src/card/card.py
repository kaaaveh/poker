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
        """Create a card from a rank and a suit."""
        return cls(int(suit) * 13 + int(rank))
    
    @classmethod
    def from_str(cls, s:str) -> "Card":
        """Parse a card from notation like 'Ah' or '2c'. """
        s = s.strip()
        if len(s) != 2:
            raise ValueError(f"Invalid card string: {s!r}")
        return cls.of(Rank.from_char(s[0]), Suit.from_char(s[1]))
    
    # display
    def __str__(self) -> str:
        return f"{self.rank.to_char()}{self.suit.to_char()}"
    
    def __repr__(self) -> str:
        return f"Card(id={self._id}, rank={self.rank}, suit={self.suit})"
    
    def pretty(self) -> str:
        return f"{self.rank.to_char()}{self.suit.to_symbol()}"
from enum import IntEnum

class Suit(IntEnum):
    CLUBS       =   0
    DIAMONDS    =   1
    HEARTS      =   2
    SPADES      =   3

    @classmethod
    def from_char(cls, ch: str) -> "Suit":
        mapping = {
            "c": cls.CLUBS,
            "d": cls.DIAMONDS,
            "h": cls.HEARTS,
            "s": cls.SPADES,
        }
        try:
            return mapping[ch.lower()]
        except KeyError:
            raise ValueError(f"Invalid suit character: {ch!r}")
    
    def to_char(self) -> str:
        return "cdhs"[self.value]
    
    def to_symbol(self) -> str:
        return "♣♦♥♠"[self.value]
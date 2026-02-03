from enum import IntEnum

class Rank(IntEnum):
    TWO     =   0
    THREE   =   1
    FOUR    =   2
    FIVE    =   3
    SIX     =   4
    SEVEN   =   5
    EIGHT   =   6
    NINE    =   7
    TEN     =   8
    JACK    =   9
    QUEEN   =   10
    KING    =   11
    ACE     =   12

    @classmethod
    def from_char(cls, ch:str) -> "Rank":
        mapping = {
            "2": cls.TWO,
            "3": cls.THREE,
            "4": cls.FOUR,
            "5": cls.FIVE,
            "6": cls.SIX,
            "7": cls.SEVEN,
            "8": cls.EIGHT,
            "9": cls.NINE,
            "T": cls.TEN,
            "J": cls.JACK,
            "Q": cls.QUEEN,
            "K": cls.KING,
            "A": cls.ACE,
        }
        try:
            return mapping[ch.upper()]
        except KeyError:
            raise ValueError(f"Invalid rank character: {ch!r}")
    

    def to_char(self) -> str:
        return "23456789TJQKA"[self.value]
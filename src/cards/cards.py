from __future__ import annotations
from typing import Iterable, Sequence

from .card.card import Card
from .rank.rank import Rank
from .suit.suit import Suit

__all__ = [
    "Card",
    "Rank",
    "Suit",
    "parse_card",
    "parse_cards",
    "format_cards",
    "ensure_unique",
    "card_ids",
]

def parse_card(s:str) -> Card:
    """Parse a single card from a 2-char string like 'Ah'"""
    return Card.from_str(s)

def parse_cards(s: str, *, separator: str | None = None, ensure_unique_cards: bool = True) -> list[Card]:
    """
    Parse multiple cards from a string.

    Examples:
        "As Kd 7c"                (default: split on whitespace)
        "As,Kd,7c"                (separator=",")
        "As|Kd|7c"                (separator="|")

    Args:
        s: input string
        separator: if None, split on whitespace; otherwise split on this separator
        ensure_unique_cards: if True, raises ValueError on duplicates

    Returns:
        list[Card]
    """
    text = s.strip()
    if not text:
        return []
    
    parts = text.split() if separator is None else [p.strip() for p in text.split(separator)]
    # filter empty chunks (e.g., "As,,Kd" with separator=",")
    parts = [p for p in parts if p]

    cards = [Card.from_str(p) for p in parts]

    if ensure_unique_cards:
        ensure_unique(cards)

    return cards

def format_cards(cards: Iterable[Card], *, separator: str = " ", pretty: bool = False) -> str:
    """Format a list of cards into a string.
    
    Example:
        [As, Kd, 7c] -> "As Kd 7c"
        pretty=True  -> "A♠ K♦ 7♣"
    """
    if pretty:
        return separator.join(c.pretty() for c in cards)
    return separator.join(str(c) for c in cards)

def ensure_unique(cards: Sequence[Card]) -> None:
    """Raise ValueError if cards are not unique."""
    if len(set(cards)) != len(cards):
        seen: set[Card] = set()
        dups: list[str] = []
        for c in cards:
            if c in seen and str(c) not in dups:
                dups.append(str(c))
            seen.add(c)
        raise ValueError(f"Duplicate cards detected: {', '.join(dups) if dups else 'unknown duplicates'}")

def card_ids(cards: Iterable[Card]) -> list[int]:
    """Convenience: convert cards to their int ids (0..51)."""
    return [c.id for c in cards]
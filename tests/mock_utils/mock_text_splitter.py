"""Mock text splitter."""

from typing import Any, List, Optional


def patch_token_splitter_newline(
    self: Any, text: str, metadata_str: Optional[str] = None
) -> List[str]:
    """Mock token splitter by newline."""
    return [] if not text else text.split("\n")


def mock_token_splitter_newline(
    text: str, metadata_str: Optional[str] = None
) -> List[str]:
    """Mock token splitter by newline."""
    return [] if not text else text.split("\n")

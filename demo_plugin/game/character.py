# from typing import Protocol

try:
    print("here")
    from typing import Protocol
except ImportError as e:
    print(str(e))
    from typing_extensions import Protocol


class GameCharacter(Protocol):
    """Basic representation of a game character."""

    def make_a_noise(self) -> None:
        """Let the character make a noise."""

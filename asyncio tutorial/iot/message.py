from dataclasses import dataclass
from enum import Enum, auto, unique


class MessageType(Enum):
    SWITCH_ON = auto()
    SWITCH_OFF = auto()
    CHANGE_BRIGHTNESS = auto()
    CHANGE_COLOR = auto()
    PLAY_SONG = auto()
    OPEN = auto()
    CLOSE = auto()
    FLUSH = auto()
    CLEAN = auto()


@dataclass
class Message:
    device_id: int
    message_type: MessageType
    data: str = ""
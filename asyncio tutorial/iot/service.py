import random
import string
import asyncio
from random import randint
from typing import Protocol

from iot.message import MessageType, Message


def generate_id(lenght: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=lenght))


class Device(Protocol):
    async def connect(self) -> None:
        ...

    async def disconnect(self) -> None:
        pass

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        pass


class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    async def register_device(self, device: Device) -> str:
        await device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    async def unregister_device(self, device_id: str) -> None:
        await self.devices[device_id].disconnect()
        del self.devices[device_id]

    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]

    async def run_program(self, program: list[Message]) -> None:
        print("==== RUNNING PROGRAM ====")
        await asyncio.gather(*[self.send_message(message) for message in program])
        print("==== PROGRAM FINISHED ====")

    async def send_message(self, message: Message) -> None:
        await self.devices[message.device_id].send_message(message.message_type, message.data)
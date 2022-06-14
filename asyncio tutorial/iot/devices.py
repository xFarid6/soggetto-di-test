from iot.message import MessageType
import asyncio


class HueLightDevice(object):
    async def connect(self) -> None:
        print("Connecting to Hue Light device")
        await asyncio.sleep(0.5)
        print("Connected to Hue Light device")
        
    async def disconnect(self) -> None:
        print("Disconnecting from Hue Light device")
        await asyncio.sleep(0.5)
        print("Disconnected from Hue Light device")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Hue Light device handling message: {message_type.name} - {data}"
        )
        await asyncio.sleep(0.5)
        print("Light device handled message")


class SmartSpeakerDevice(object):
    async def connect(self) -> None:
        print("Connecting to speaker")
        await asyncio.sleep(0.5)
        print("Connected to speaker")
        
    async def disconnect(self) -> None:
        print("Disconnecting from speaker")
        await asyncio.sleep(0.5)
        print("Disconnected from speaker")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Smart Speaker handling message: {message_type.name} - {data}"
        )
        await asyncio.sleep(0.5)
        print("Smart Speaker handled message")


class SmartToiletDevice(object):

    async def connect(self) -> None:
        print("Connecting to toilet")
        await asyncio.sleep(0.5)
        print("Connected to toilet")

    async def disconnect(self) -> None:
        print("Disconnecting from toilet")
        await asyncio.sleep(0.5)
        print("Disconnected from toilet")

    async def send_message(self, message_type: MessageType, data: str = "") -> None:
        print(
            f"Smart toilet handling message of type {message_type.name} with data {data}"
        )
        await asyncio.sleep(0.5)
        print("Smart toilet handled message")
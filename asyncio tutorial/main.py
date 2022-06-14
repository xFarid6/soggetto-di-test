# threads can share memory, can have one or more threads
# processes can have max 1, each has separate memory

# threads are used whenever there is to wait for a result
# problems:
# 1. threads are not parallel
# 2. harder to read code than
# 3. have problems with concurrency, memory racing, deadlock
# 4. uses more cpu to keep track of everything that happens

# an alternative to threads is asyncio
# asyncio is a library that allows you to run a program in the background
# promises in javascript and futures in python
# asyncio is a coroutine library

# lets write some code that runs asyncronously

from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService
from typing import Awaitable, Any
import asyncio

async def run_sequence(*functions: Awaitable[Any]) -> None: 
    for function in functions:
        await function

async def run_parallel(*functions: Awaitable[Any]) -> None: 
    await asyncio.gather(*functions)

async def main() -> None:
    # create a IOT Service object
    iot_service = IOTService()

    # create and register a few devices
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()
    
    # hue_light_id = await iot_service.register_device(hue_light)
    # speaker_id = await iot_service.register_device(speaker)
    # toilet_id = await iot_service.register_device(toilet)

    hue_light_id, speaker_id, toilet_id = await asyncio.gather(
        iot_service.register_device(hue_light),
        iot_service.register_device(speaker),
        iot_service.register_device(toilet),
    )

    # create a few programs
    wake_up_programs = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Happy Birthday"),
    ]

    sleep_programs = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(toilet_id, MessageType.FLUSH),
        Message(toilet_id, MessageType.CLEAN),
    ]

    # run the programs
    await iot_service.run_program(wake_up_programs)
    # await iot_service.run_program(sleep_programs)
    await run_parallel(
        iot_service.send_message(Message(hue_light_id, MessageType.SWITCH_OFF)), 
        iot_service.send_message(Message(speaker_id, MessageType.SWITCH_OFF)),
        run_sequence(
            iot_service.send_message(Message(toilet_id, MessageType.FLUSH)),
            iot_service.send_message(Message(toilet_id, MessageType.CLEAN)),
        ),
        run_sequence(
            iot_service.send_message(Message(toilet_id, MessageType.FLUSH)),
            iot_service.send_message(Message(toilet_id, MessageType.CLEAN)),
        ),
    )


if __name__ == '__main__':
    # create a list of devices
    asyncio.run(main())
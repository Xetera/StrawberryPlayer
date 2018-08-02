from typing import Union
from websocket.packet import Packet


async def dispatch(websocket, packet: Union[str, dict, Packet]) -> None:
    if isinstance(packet, str):
        return await websocket.send(packet)
    return await websocket.send(packet.serialize())


async def receive(websocket) -> Packet:
    pack = await websocket.recv()
    return Packet(pack)

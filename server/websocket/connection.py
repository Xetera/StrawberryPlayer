from typing import Union

from utils.logging import logger
from websocket.packet import Packet
import websockets

clients = set()
socket = websockets.WebSocketCommonProtocol


async def dispatch(websocket, packet: Union[str, dict, Packet]) -> None:
    if isinstance(packet, str):
        return await websocket.send(packet)
    return await websocket.send(packet.serialize())


async def receive(websocket) -> Packet:
    pack = await websocket.recv()
    return Packet(pack)


def register_client(websocket: socket):
    logger.info('New client has connected')
    clients.add(websocket)


def unregister_client(websocket: socket):
    logger.info('A client has lost connection')
    clients.remove(websocket)

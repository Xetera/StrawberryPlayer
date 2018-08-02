import json
from typing import Optional, Union
from utils.logging import logger


class Packet:
    """
    Serializable object for sending and receiving messages
    from the client
    """
    def __init__(self, incoming: Optional[str] = None, **kwargs):
        if isinstance(incoming, Packet):
            self.header = incoming.header
            self.body = incoming.body
            self.user = incoming.user
            return

        elif 'body' in kwargs and 'header' in kwargs:
            self.header = kwargs.get('header')
            self.body = kwargs.get('body')
            self.user = kwargs.get('user')
            return

        try:
            if not incoming:
                raise ReferenceError("Message body is empty.")

            packet = json.loads(incoming)
            self.header: str = packet['header']
            self.body: Union[str, list] = packet['body']

            logger.debug(f'Created a new packet with size {len(self.body)}')
        except (TypeError, IndexError) as e:
            logger.error(e)
            raise BaseException("Invalid packet body")

    @property
    def is_valid(self):
        return self.header and self.body

    def __repr__(self):
        return self.serialize()

    def serialize(self) -> str:
        info = {
            'header': self.header,
            'body': self.body
        }
        out = json.dumps(info)
        logger.debug(f'Serialized an object to size {len(out)}')
        return out

    def __eq__(self, other):
        return self.serialize() == other.serialize()


async def dispatch(websocket, packet: Union[str, dict, Packet]) -> None:
    if isinstance(packet, str):
        return await websocket.send(packet)
    return await websocket.send(packet.serialize())


def receive(websocket) -> Packet:
    pack = websocket.recv()
    return Packet(pack)

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
            self.event = incoming.event
            self.body = incoming.body
            self.user = incoming.user
            return

        elif 'body' in kwargs and 'event' in kwargs:
            self.event = kwargs.get('event')
            self.body = kwargs.get('body')
            self.user = kwargs.get('user')
            return

        try:
            if not incoming:
                raise ReferenceError("Message body is empty.")

            packet = json.loads(incoming)
            self.event: str = packet['event']

            try:
                self.body: Union[str, list] = json.loads(packet['body'])
            except ValueError:
                self.body: Union[str, list] = packet['body']

            self.user: str = packet.get('user')
            logger.debug(f'Created a new packet with size {len(self.body)}')
        except (TypeError, IndexError) as e:
            logger.error(e)
            raise BaseException("Invalid packet body")

    @property
    def is_valid(self):
        return self.event and self.body

    def __repr__(self):
        return self.serialize()

    def serialize(self) -> str:
        info = {
            'event': self.event,
            'body': self.body
        }
        if isinstance(self.body, dict):
            info['body'] = json.dumps(self.body)

        out = json.dumps(info)
        logger.debug(f'Serialized an object to size {len(out)}')
        return out

    def get(self, attr: str):
        """Fetches values from body"""
        print(self.body)
        if isinstance(self.body, dict):
            return self.body[attr]
        return self.body

    def __eq__(self, other):
        return self.serialize() == other.serialize()

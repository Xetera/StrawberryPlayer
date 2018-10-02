import json

from utils.logging import logger
from websocket.connection import dispatch
from websocket.packet import Packet


async def send_new_song(socket, song_hash: str, metadata: dict) -> None:
    packet = Packet(
        event='download',
        body=json.dumps({
            'song': song_hash,
            'metadata': metadata
        })
    )
    await dispatch(socket, packet)
    logger.debug(f'Sent a downloaded song {song_hash}')

import asyncio
import websockets
import youtube_dl
import os

from config import get_save_location
from player.player import add_song
from utils.logging import logger
from youtube import download
from websocket.packet import Packet
from websocket.connection import dispatch, receive
import config


async def handler(websocket: websockets, path):
    # if not isinstance(websocket.recv(), str):
    #     return

    packet: Packet = await receive(websocket)

    if packet.header not in config.valid_requests:
        return logger.error(f'Received unrecognized request')

    logger.info(f'Received a {packet.header} request from {packet.user}')
    if packet.header == 'download':
        with youtube_dl.YoutubeDL(config.ytdl_opts) as ytdl:
            file = await download.download_song(ytdl, packet.body, packet.user)
    elif packet.header == 'search':
        with youtube_dl.YoutubeDL(config.ytdl_opts) as ytdl:
            info = await download.fetch_info(ytdl, packet.body)
            response = Packet(header=packet.header, body=info)
            await dispatch(websocket, response)


if __name__ == '__main__':
    server = os.environ.get('IP_ADDRESS', 'localhost')
    port = 10000
    logger.info(f'Starting server at {server}:{port}')
    logger.info(f'Saving media at {get_save_location()}')

    start_server = websockets.serve(handler, server, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

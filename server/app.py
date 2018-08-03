import asyncio
import websockets
import os

from config import get_save_location
from utils.logging import logger
from websocket.exception import WebsocketRequestException
from websocket.packet import Packet
from websocket.connection import dispatch, receive, clients
import config
from websocket.events import on_download, on_search, on_pause, on_play, on_skip


async def handler(websocket: websockets.WebSocketCommonProtocol, path):
    # A copy of this callback is ran for each individual connection
    while not websocket.closed:
        packet: Packet = await receive(websocket)

        logger.info(f'Received a {packet.event} request from {packet.user}')
        event_params = (websocket, packet)

        if packet.event == 'download':
            await on_download(*event_params)
        elif packet.event == 'search':
            await on_search(*event_params)
        elif packet.event == 'pause':
            await on_pause(*event_params)
        elif packet.event == 'play':
            await on_play(*event_params)
        elif packet.event == 'skip':
            await on_skip(*event_params)
        else:
            logger.error(f'Received unrecognized request')
            error = WebsocketRequestException(
                event=packet.event,
                body='Invalid request'
            )
            return await dispatch(websocket, error)


if __name__ == '__main__':
    ip = os.environ.get('IP_ADDRESS', 'localhost')
    port = os.environ.get('PORT', '100000')

    logger.info(f'Starting server at {ip}:{port}')
    logger.info(f'Saving media at {get_save_location()}')

    server = websockets.serve(handler, ip, port)
    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()

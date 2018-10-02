import asyncio
import websockets
import youtube_dl
import config
from player.player import toggle_status, async_skip
from websocket.connection import dispatch
from youtube import download
from websocket.packet import Packet
from youtube.utils import extract_song_metadata

socket = websockets.WebSocketCommonProtocol


async def on_download(websocket: socket, packet: Packet):
    with youtube_dl.YoutubeDL(config.get_opts()) as ytdl:
        loop = asyncio.get_event_loop()
        file = await download.download_song(socket, ytdl, packet.get('song'), packet.user, loop)


async def on_search(websocket: socket, packet: Packet):
    with youtube_dl.YoutubeDL(config.get_opts()) as ytdl:
        song_id = packet.get('id')
        song = packet.get('song')

        info = await download.fetch_info(websocket, ytdl, song, song_id)
        metadata = extract_song_metadata(info)

        response = Packet(
            event=packet.event, body={
                'metadata': metadata,
                'id': song_id
            }
        )
        await dispatch(websocket, response)


async def on_pause(websocket: socket, packet: Packet):
    await toggle_status()


async def on_play(websocket: socket, packet: Packet):
    await toggle_status()


async def on_skip(websocket: socket, packet: Packet):
    await async_skip()

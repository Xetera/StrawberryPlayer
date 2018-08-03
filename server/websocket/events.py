import websockets
import youtube_dl
import config
from player.player import toggle_status
from websocket.connection import dispatch
from youtube import download
from websocket.packet import Packet

socket = websockets.WebSocketCommonProtocol


async def on_download(websocket: socket, packet: Packet):
    with youtube_dl.YoutubeDL(config.get_opts()) as ytdl:
        file = await download.download_song(ytdl, packet.body, packet.user)


async def on_search(websocket: socket, packet: Packet):
    with youtube_dl.YoutubeDL(config.get_opts()) as ytdl:
        info = await download.fetch_info(ytdl, packet.body)
        response = Packet(header=packet.header, body=info)
        await dispatch(websocket, response)


async def on_pause(websocket: socket, packet: Packet):
    await toggle_status()


async def on_play(websocket: socket, packet: Packet):
    await toggle_status()


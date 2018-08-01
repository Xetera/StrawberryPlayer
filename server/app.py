import asyncio
import websockets
import youtube_dl
import os

from utils.logging import logger
from youtube import download
from utils.packet import stringify

ytdl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '140'
    }]
}


async def hello(websocket, path):
    print(path)
    song = await websocket.recv()

    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        something = await download.fetch_info(ytdl, song)
        await websocket.send(stringify(something))
        # result = ytdl.extract_info(song, download=False)
        # video = None
        # if 'entries' in result:
        #     video = result['entries'][0]
        # else :
        #     video = result
        # video_url =



if __name__ == '__main__':
    server = os.environ.get('IP_ADDRESS', 'localhost')
    port = 10000
    logger.info('Starting server at {server}:{port}')
    start_server = websockets.serve(hello, server, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

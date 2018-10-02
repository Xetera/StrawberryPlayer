import asyncio
import youtube_dl
from datetime import datetime
import hashlib

from config import get_save_location
from player.player import add_song
from utils.logging import logger
from websocket.dispatch import send_new_song
from youtube.utils import extract_song_metadata


async def async_download(client, search):
    return client.download(search)


async def async_extract_info(client, search, download=False):
    return client.extract_info(search, download)


async def fetch_info(socket, client: youtube_dl.YoutubeDL, song: str, song_hash: str, ip: str = 'unknown user') -> dict:
    """
    Used for fetching only the information of a song from youtube
    :param client: YoutubeDL client
    :param song: song name searched as string
    :param ip: optional user identifier for logging
    :return: YoutubeDL search result response
    """
    logger.info(f'Got an extract request for "{song}" from [{ip}]')

    start = datetime.now()
    info = client.extract_info(f'ytsearch:{song}', download=False)
    delta = datetime.now() - start

    logger.info(f'Extracted information for "{song}" in {delta.seconds} seconds')
    return info


async def download_with_info(client, search_string):
    try:
        info = await asyncio.gather(
            async_download(client, [search_string]),
            async_extract_info(client, search_string, download=False)
        )
        return info
    except PermissionError:
        pass


async def download_song(socket, client: youtube_dl.YoutubeDL, song: str, song_hash: str,
                        loop: asyncio.AbstractEventLoop,
                        ip: str = 'unknown user'):
    logger.info(f'Downloading song {song} at {get_save_location()} by {ip}')

    search_string = f'ytsearch:{song}'

    start = datetime.now()
    response = await asyncio.ensure_future(download_with_info(client, search_string))
    metadata = extract_song_metadata(response[-1])

    await send_new_song(socket, song_hash, metadata)

    delta = datetime.now() - start

    logger.info(f'Downloaded in {delta.seconds} seconds')

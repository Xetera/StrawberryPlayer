import youtube_dl
from datetime import datetime
import hashlib

from config import get_save_location
from player.player import add_song
from utils.logging import logger
from youtube.utils import extract_file_metadata


async def fetch_info(client: youtube_dl.YoutubeDL, song: str, ip: str = 'unknown user') -> dict:
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


async def download_song(client: youtube_dl.YoutubeDL, song: str, ip: str = 'unknown user'):
    logger.info(f'Downloading song {song} at {get_save_location()} by {ip}')

    start = datetime.now()
    try:
        client.download([f'ytsearch:{song}'])
    except PermissionError:
        pass
    delta = datetime.now() - start

    logger.info(f'Downloaded in {delta.seconds} seconds')

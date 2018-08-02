import youtube_dl
from datetime import datetime

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


async def download_song(client: youtube_dl.YoutubeDL, song: str, ip: str = 'unknown user') -> dict:
    logger.info(f'Downloading song {song} at {get_save_location()} by {ip}')

    start = datetime.now()
    file = client.extract_info(f'ytsearch:{song}')
    delta = datetime.now() - start

    parsed_file = extract_file_metadata(file)
    print(parsed_file)
    logger.info(f'Downloaded "{song}" in {delta.seconds} seconds')
    logger.info(f'Adding {song} to playlist')
    return file

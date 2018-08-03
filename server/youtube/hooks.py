import os

import asyncio

from player.player import add_song
from utils.logging import logger


async def on_file_download_finish(obj: dict):
    file_tuple = os.path.split(os.path.abspath(obj['filename']))
    file_name = list(file_tuple).pop()
    logger.info(f'Adding {file_name} to playlist')
    await add_song(file_name)


def progress_hook(obj: dict):
    if obj['status'] == 'finished':
        loop = asyncio.get_event_loop()
        loop.create_task(on_file_download_finish(obj))
    elif obj['status'] == 'download':
        total = obj['total_bytes']
        downloaded = obj['downloaded_bytes']
        print(f'downloaded: {(downloaded/total) * 100}%')

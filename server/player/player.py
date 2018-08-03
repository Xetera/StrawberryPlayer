from os import path

import asyncio
import vlc

import player.events
from config import get_save_location
from player.instances import queue, player, tracker, vlc_instance, manager
from utils.logging import logger


async def add_song(save_location: str) -> vlc.MediaListPlayer:
    """

    :param save_location: path to the file to add
    :return:
    """
    file_path = path.join(get_save_location(), save_location)
    media = vlc_instance.media_new(file_path)
    queue.add_media(media)
    # player.audio_set_volume(100)
    tracker.set_media_list(queue)
    await check_player()
    return tracker


async def remove_song(media: vlc.Media) -> bool:
    """
    Removes a song from the queue, returns True if successful
    :param media: Media to remove
    :return: bool - whether action was successful or not
    """
    index = queue.index_of_item(media)
    if index == -1:
        return False
    queue.remove_index(index)
    await check_player()
    return True


async def toggle_status():
    if tracker.is_playing():
        await async_pause()
    else:
        await check_player()


async def check_player():
    if not queue.count():
        return logger.info('Cannot play anything, playlist is empty')

    if not player.is_playing():
        await async_play()


async def async_play():
    tracker.play()


async def async_pause():
    tracker.pause()


async def async_skip():
    tracker.next()

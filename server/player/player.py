import vlc
from .instances import queue, player, tracker, vlc_instance


def add_song(path: str) -> vlc.MediaListPlayer:
    """

    :param path: path to the file to add
    :return:
    """
    media = vlc_instance.media_new(path)
    queue.add_media(media)
    # player.audio_set_volume(100)
    tracker.set_media_list(queue)
    return tracker


def remove_song(media: vlc.Media) -> bool:
    """
    Removes a song from the queue, returns True if successful
    :param media: Media to remove
    :return: bool - whether action was successful or not
    """
    index = queue.index_of_item(media)
    if index == -1:
        return False
    queue.remove_index(index)
    return True

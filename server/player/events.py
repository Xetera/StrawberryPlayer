import vlc
from player.instances import manager, queue
from utils.logging import logger


def on_media_player_end_reached(something):
    print(something)
    logger.info('Reached end of song ')
    queue.remove_index(0)


print('Attaching event callback')
manager.event_attach(vlc.EventType.MediaPlayerEndReached, on_media_player_end_reached)

import vlc
vlc_instance: vlc.Instance = vlc.Instance()
queue: vlc.MediaList = vlc_instance.media_list_new()
player: vlc.MediaPlayer = vlc_instance.media_player_new()
tracker: vlc.MediaListPlayer = vlc_instance.media_list_player_new()
manager: vlc.EventManager = player.event_manager()

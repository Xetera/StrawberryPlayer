import os
from os import path

from dotenv import load_dotenv


load_dotenv()


def get_save_location():
    return os.environ.get('DOWNLOAD_LOCATION', '/home/pi/music')


def get_opts() -> dict:
    from youtube.hooks import progress_hook
    return {
        'format': '140',
        'outtmpl': path.join(get_save_location(), '%(title)s.%(ext)s'),
        # 'postprocessors': [{
        #     'key': 'FFmpegExtractAudio',
        #     'preferredcodec': 'mp3',
        #     'preferredquality': '140'
        # }],
        'progress_hooks': [progress_hook]
    }



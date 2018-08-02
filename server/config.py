import os
from os import path

from dotenv import load_dotenv

from youtube.hooks import progress_hook

load_dotenv()


def get_save_location():
    return os.environ.get('DOWNLOAD_LOCATION', '~/music')


ytdl_opts = {
    'format': '140',
    'outtmpl': path.join(get_save_location(), '%(title)s-%(id)s.%(ext)s'),
    # 'postprocessors': [{
    #     'key': 'FFmpegExtractAudio',
    #     'preferredcodec': 'mp3',
    #     'preferredquality': '140'
    # }],
    'progress_hooks': [progress_hook]
}

valid_requests = [
    'search',
    'download'
]



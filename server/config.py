import os
ytdl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '140'
    }]
}

valid_requests = [
    'search',
    'download'
]


def get_save_location():
    return os.environ.get('DOWNLOAD_LOCATION', '~/music')

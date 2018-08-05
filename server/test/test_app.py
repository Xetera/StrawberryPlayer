import youtube_dl
from config import get_opts


ytdl_client = youtube_dl.YoutubeDL(get_opts())
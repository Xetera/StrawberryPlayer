import youtube_dl
from datetime import datetime
from utils.logging import logger


async def fetch_info(client: youtube_dl.YoutubeDL, song: str, ip: str = 'unknown user') -> dict:
    logger.info(f'Got an extract request for {song} from {ip}')
    start = datetime.now()
    something = client.extract_info(f'ytsearch:{song}', download=False)
    delta = datetime.now() - start
    logger.info(f'Extracted information for {song} in {delta}ms')
    return something

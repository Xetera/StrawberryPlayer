import string

def extract_song_metadata(ytdl_response: dict) -> dict:
    entries = ytdl_response['entries']
    if ytdl_response['_type'] == 'playlist':
        return entries[0]
    return entries


def strip_to_unicode(name: str) -> str:
    printable = set(string.printable)
    return str(filter(lambda char: char in printable, name))

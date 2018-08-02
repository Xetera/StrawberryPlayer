def extract_file_metadata(ytdl_response: dict) -> dict:
    entries = ytdl_response['entries']
    if isinstance(entries, list):
        return entries[0]
    return entries

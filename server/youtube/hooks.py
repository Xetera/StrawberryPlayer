def progress_hook(obj: dict):
    try:
        total = obj['total_bytes']
        downloaded = obj['downloaded_bytes']
        print(f'downloaded: {(downloaded/total) * 100}%')
    except KeyError:
        print(obj)

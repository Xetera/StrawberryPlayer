import asyncio
import websockets
import youtube_dl
import os
import json

ytdl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '140'
    }]
}


async def hello(websocket, path):
    song = await websocket.recv()

    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        something = ytdl.extract_info(f'ytsearch:{song}', download=False)
        print(something)
        await websocket.send(json.dumps(something))
        # result = ytdl.extract_info(song, download=False)
        # video = None
        # if 'entries' in result:
        #     video = result['entries'][0]
        # else :
        #     video = result
        # video_url =

    print(f"> {greeting}")


if __name__ == '__main__':
    server = os.environ.get('IP_ADDRESS', 'localhost')
    port = 10000
    print(f'Starting server at {server}:{port}')
    start_server = websockets.serve(hello, server, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

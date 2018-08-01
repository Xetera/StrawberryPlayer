import asyncio
import websockets
import youtube_dl

ytdl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '140'
    }],
    '--default-search': 'ytseach'
}


async def hello(websocket, path):
    song = await websocket.recv()

    with youtube_dl.YoutubeDL(ytdl_opts) as ytdl:
        something = ytdl.download([f'ytsearch:{song}'])
        print(something)
        # result = ytdl.extract_info(song, download=False)
        # video = None
        # if 'entries' in result:
        #     video = result['entries'][0]
        # else :
        #     video = result
        # video_url =

    print(f"> {greeting}")


start_server = websockets.serve(hello, 'localhost', 10000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

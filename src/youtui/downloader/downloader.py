import yt_dlp

def on_progress(d):
    if d["status"] == 'downloading' and d['total_bytes']:
        print(d['filename'])
        print((d['downloaded_bytes']/d['total_bytes']) * 100)
        print('---------------------------------------------')

yt_opts = {
    # 'format': 'bestaudio',
    'format': 'best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': True,
    # 'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'opus'
    #     },
    # ],
    'outtmpl': '%(title)s-%(id)s.%(ext)s',
    'quiet': True,
    'no_warnings': True,
    "noprogress": True,
    'progress_hooks': [on_progress],
    # 'writesubtitles': True,
}

ydl = yt_dlp.YoutubeDL(yt_opts)

# with yt_dlp.YoutubeDL(yt_opts) as ydl:
#     # ydl.download("https://youtu.be/ONiE-FEb3Ys?si=AxRTgay1UpNreenq")
#     ydl.download("https://www.youtube.com/watch?v=lv1_-RER4_I")

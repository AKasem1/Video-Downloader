import yt_dlp

save_path = input("Where do you want to save the video? ")
video_link = input("What is the video url? ")

try:
    ydl_opts = {'outtmpl': f'{save_path}/%(title)s.%(ext)s'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_link])
    print("Download is completed successfully")
except Exception as e:
    print(f"An error has occurred: {e}")

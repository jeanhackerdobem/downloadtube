from pytube import YouTube

url = "https://youtu.be/"

yt = YouTube(url)

video_stream = yt.streams.get_highest_resolution()

video_stream.download()

print("DOWNLOAD COMPLETO!\nSeu vídeo está na pasta/diretório local!")

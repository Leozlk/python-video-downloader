#Made by @Leozlk - 2023
import yt_dlp

#get the list in the main folder
lista = open('lista.txt', 'r')
Lines = lista.readlines()

#options about download quality
ydl_opts = {
    'format': 'best',
    'nooverwrites': True,
}
# for every line in the list.txt
for line in Lines:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(line)

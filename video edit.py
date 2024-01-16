from moviepy.editor import clips_array,TextClip
import os
import random
from moviepy.config import change_settings
from moviepy.editor import VideoFileClip
from moviepy.editor import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
import requests
import uplaod_video_instagram
import winsound
def chess_board():
    headers = {'User-Agent': 'Chess.py (Python 3.7) (username: Ahmed_chebb1; contact: ssjzchebbi@gmail.com)'}
    x = requests.get(" https://api.chess.com/pub/puzzle/random",headers=headers)
    return x.json()

L=chess_board()
print(L)
response = requests.get(L['image'])
image_data = response.content
file_path = 'boards/'+L['title']+'.png'
with open(file_path, 'wb') as file:
    file.write(image_data)
change_settings({"IMAGEMAGIC_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe" })
folder_path = 'edits/'
video_files = [file_name for file_name in os.listdir(folder_path) if file_name.lower().endswith(('.mp4'))]
random_int = random.randint(0, len(video_files)-1)
fen=L["fen"].split()
ftp=""
if(fen[1]=='w'):
    ftp="white to play"
else:
    ftp="black to play"
clip = VideoFileClip("edits/"+video_files[random_int])
image_clip = ImageClip(file_path)
clip1 = clip.resize((480,360))
w,h = clip1.size
duration = clip.duration
title = file_path.replace("boards/","").replace(".png","")
PAD=0
if len(title)>14:
    T="Puzzle name :"+'\n'+title
    PAD=25
else:
    T="Puzzle name :"+title
print(T,video_files[random_int])
puzzle_title = TextClip(T,color='white', font="BSK.ttf",bg_color="black" , kerning=5,fontsize=21,align="west").set_position((17,485)).set_duration(duration)
first_to_play = TextClip(ftp,color='white', font="BSK.ttf",bg_color="black" , kerning=5,fontsize=18).set_position((17,513+PAD)).set_duration(duration)
image_clip = image_clip.set_position(100,500)
image_clip = image_clip.set_duration(duration)
final_clip = clips_array([ [image_clip],[clip1]])
final_clip = CompositeVideoClip([final_clip , puzzle_title, first_to_play])
final_clip1=final_clip.resize((1080 ,1920))
final_clip1.write_videofile("here2.mp4")
uplaod_video_instagram.upload_insta("here2.mp4", "follow for more chess puzzles ♟️\n\nChess puzzle Link: "+L["url"]+"\n\n#chess #chessgame #chessboard #chessplayer #elitechess #grandmaster #chesslife #puzzle #boardgame #playingchess #brilliant")
winsound.Beep(1000,1000)
import  praw 
import syllables
from gtts import gTTS
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})

from moviepy.editor import *
import os

                 

reddit = praw.Reddit(
    client_id="rAIDYUguYJ4f-b17HpRLHg",
    client_secret="",
    user_agent="my user agent",
)


#global variables
x = 0
str_post = ""
clip = VideoFileClip("skib.mp4") 
start_time = 0 
clip_num = 0  


#takes top submission and top 5 comments and appends to a string
for submission in reddit.subreddit("ohio").hot(limit=1):

    str_post += (submission.title) 

    for comment in submission.comments:

        str_post += (comment.body + " ")
        
        x += 1 
        if x == 5:
            x = 0 
            break

#splits string into list of words
str_post = str_post.replace("."," ")
arr_post = str_post.split()


def create_video(word, start_time, syl, clip_num):
    
    print(clip_num)
    arr_post[clip_num] = TextClip(word , fontsize = 100, color = 'white', stroke_color = 'black', stroke_width= 3)  
    arr_post[clip_num] = arr_post[clip_num].set_pos('center').set_start(start_time).set_duration(syl)  
    
  
    

for word in arr_post:
    
    syl = syllables.estimate(word)*0.26
    create_video(word,start_time,syl,clip_num)
    start_time += syl
    clip_num += 1



tts = gTTS(text=str_post, lang='en')
tts.save('output.mp3')


audio = AudioFileClip("output.mp3")
video = CompositeVideoClip([clip, *arr_post]).set_audio(audio)

video.write_videofile("dopdop.mp4", codec="libx264")




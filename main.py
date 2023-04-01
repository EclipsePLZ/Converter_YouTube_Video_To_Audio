import os
from pytube import YouTube
import telebot
from auth_data import token
from bot import telegram_bot



def video_to_mp3(url_video):
    
    try:
        print('Connection start')
        yt = YouTube(url_video)
    except:
        return 'Connection error, try again!'
    
    audio_stream = yt.streams.filter(only_audio=True).first()
    
    if not os.path.exists(r'.\Audios'):
        os.mkdir(r'.\Audios')
    
    try:
        audio_file = audio_stream.download(output_path=r'.\Audios')
        print('Audio file downloaded successfully')
    except:
        return 'Error downloading the file!'
    
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    return yt.title + " has been successfully downloaded."


def main():
    telegram_bot(token)


if __name__ == '__main__':
    main()
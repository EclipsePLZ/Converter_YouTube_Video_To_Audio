import os
from pytube import YouTube
import telebot
from auth_data import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    
    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Hello friend! Enter the command!")
        
    @bot.message_handler(content_types=["text"])
    def send_audio(message):
        if 'youtube.com' in message.text or 'youtu.be' in message.text:
            url_video = message.text
            try:
                yt = YouTube(url_video)
                audio_stream = yt.streams.filter(only_audio=True).first()
                
                if not os.path.exists('Audios'):
                    os.mkdir('Audios')

                audio_file = audio_stream.download(output_path='Audios')
                base, ext = os.path.splitext(audio_file)
                new_file = base + '.mp3'
                
                if os.path.exists(new_file):
                    os.remove(new_file)
                
                os.rename(audio_file, new_file)
                
                with open(new_file, 'rb') as audio:
                    bot.send_audio(message.chat.id, audio)
                    
                os.remove(new_file)
            except Exception as ex:
                print(ex)
                bot.send_message(message.chat.id, "Damn... Something was wrong...")
        else:
            bot.send_message(message.chat.id, "Whaaat??? I don't know what to do about it!")
    
    bot.polling()
    
    
def main():
    telegram_bot(token)


if __name__ == '__main__':
    main()
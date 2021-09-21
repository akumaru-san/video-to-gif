import telebot
from moviepy.editor import VideoFileClip
import os

bot = telebot.TeleBot('YOUR BOT TOKEN')


@bot.message_handler(commands=['start'])
def start(msg):
	bot.send_message(msg.chat.id,'Assalomu alaykum\n\nBot siz yuborgan videoni Gif sifatida yuboradi. Marhamat video yuboring!')

@bot.message_handler(content_types=['video'])
def convert(msg):
	bot.send_message(msg.chat.id,'Kuting bu biroz vaqt olishi mumkin!')
	try:
		file_id = msg.video.file_id
		file = bot.get_file(file_id)
		file_path = file.file_path
		s = bot.download_file(file_path)
		with open(f'{msg.chat.id}.mp4', 'wb') as new_file:
			new_file.write(s)
		with VideoFileClip(f'{msg.chat.id}.mp4') as clip:
			clip.write_gif(f"{msg.chat.id}.gif",fps=10)
		with open(f"{msg.chat.id}.gif",'rb') as gif:
			bot.send_animation(msg.chat.id,gif)
		os.unlink(f'{msg.chat.id}.mp4')
		os.unlink(f'{msg.chat.id}.gif')
	except Exception as ex:
		bot.send_message(msg.chat.id,'Xato... , Shartlarni to\'g\'ri bajaring!')
		print(ex)
bot.polling(none_stop=True)

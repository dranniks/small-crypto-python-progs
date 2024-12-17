import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup
import random

bot = telebot.TeleBot("6583520781:AAHAI18SL0V_PyXu_rkHh9ld_YvFd-wiWoY")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Хочу котика")
    
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Нажми на кнопку и я отправлю тебе котика!".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Хочу котика"):
        msg = 'p'
        while(msg[-1] == 'p'):
            url = "https://ru.freepik.com/photos/котики"
            response = requests.get(url)
        
            if response.status_code != 200:
                print(f"Ошибка при запросе страницы: {response.status_code}")
                return None
            
            soup = BeautifulSoup(response.text, 'html.parser')

            images = soup.find_all('img')
            
            if not images:
                print("Изображения не найдены.")
                return None
            
            image_urls = [img['src'] for img in images if 'src' in img.attrs]
            
            absolute_image_urls = []
            for img_url in image_urls:
                if img_url.startswith('http'):
                    absolute_image_urls.append(img_url)
                else:
                    absolute_image_urls.append(requests.compat.urljoin(url, img_url))

            msg = random.choice(absolute_image_urls)
        print(msg)
        bot.send_photo(message.chat.id, msg)

bot.polling(none_stop=True)
import telebot
import api
import citis
from config import TOKEN
from business_logic import func

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    mess = (f'Привет, <b>{message.from_user.first_name}</b>!\n'
            f'Добро пожаловать в бота для подбора одежды при разных погодных условиях!\n'
            f'Напиши город в котором ты живёшь.'
            )
    # keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    # button1 = telebot.types.KeyboardButton(text="Калининград")
    # button2 = telebot.types.KeyboardButton(text="Москва")
    # button3 = telebot.types.KeyboardButton(text="Санкт Петербург")
    # keyboard.add(button1, button2, button3)
    # bot.send_message(chat_id, mess, parse_mode='HTML', reply_markup=keyboard)
    bot.send_message(chat_id, mess, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def user_city(message):
    weather_conditions = []
    w = api.weather_by_city(message.text)

    if message.text in citis.cities:
        weather_conditions.append(f'Температура в городе {w["name"]}: {w["main"]["temp"]}°C')
        weather_conditions.append(f'Описание погоды: {w["weather"][0]["description"]}')
        weather_conditions.append(f'Влажность: {w["main"]["humidity"]}%')
        weather_conditions.append(f'Давление: {w["main"]["pressure"]} мм рт.ст.')
        weather_conditions.append(f'Скорость ветра: {w["wind"]["speed"]} м/с')
        weather_conditions.append(f'Направление ветра: {w["wind"]["deg"]}°')
        weather_conditions.append(f'Дата и время получения данных: '
                                  f'{api.current_date}, {api.current_time.replace(microsecond=0)}'
                                  )
        bot.send_message(message.chat.id, '\n'.join(weather_conditions))
        bot.send_message(message.chat.id, f'{func((w["main"]["temp"]))}')
    else:
        bot.send_message(message.chat.id, 'Такого города нет в списке, попробуй снова!')

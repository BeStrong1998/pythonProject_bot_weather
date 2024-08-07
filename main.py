from bot import bot


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
    # bot.polling(none_stop=True)
    print('Бот остановлен!')

import logging
import random
from aiogram import Bot, Dispatcher, types

API_TOKEN = '5700299275:AAFfnzmRIC8bjdb5ClFxEkFIsDM-Gny_yhA'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

min_number = 1
max_number = 100
secret_number = random.randint(min_number, max_number)


@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    global secret_number
    secret_number = random.randint(min_number, max_number)
    await message.reply("Добро пожаловать в игру 'Угадай число'! Я загадал число от 1 до 100. Попробуйте угадать!")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("Правила игры: Я загадываю число от 1 до 100. Вы должны угадать это число, отправляя мне свои предположения. "
                        "Я буду давать вам подсказки, говоря 'Мало' или 'Много'.")


@dp.message_handler()
async def guess_number(message: types.Message):
    try:
        guess = int(message.text)

        if guess < min_number or guess > max_number:
            await bot.send_message(message.chat.id, "Число должно быть в диапазоне от 1 до 100.")
        else:
            if guess < secret_number:
                await bot.send_message(message.chat.id, "Мало. Попробуйте ещё раз.")
            elif guess > secret_number:
                await bot.send_message(message.chat.id, "Много. Попробуйте ещё раз.")
            else:
                await bot.send_message(message.chat.id, "Поздравляю! Вы угадали число!")
                await start_game(message)  # новая игра

    except ValueError:
        await bot.send_message(message.chat.id, "Пожалуйста, введите число.")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)

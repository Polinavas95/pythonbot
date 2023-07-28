import os
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token=os.environ.get('API_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет!\nЯ бот от СберКлик!\nВведи сумму кредита и сумму "
                        "первоначального взноса через пробел в одну строку")


@dp.message_handler()
async def echo(message: types.Message):
    cost, anitial_fee = message.text.split()
    cost = int(cost)
    anitial_fee = (int(anitial_fee))
    if isinstance(cost, int | float) and (anitial_fee * 0.15) < cost:
        await message.answer('Вы можете подарить онлайн-заявку на ипотеку на сайте\n'
                             'https://domclick.ru/ipoteka/programs/onlajn-zayavka')
    else:
        await message.answer('Неверный формат данных или слишком маленький первоначальный взнос. Попробуйте еще раз.\n'
                             'Введи сумму кредита и сумму первоначального взноса через пробел в одну строку')


if __name__ == '__main__':
    print("Start chat bot")
    executor.start_polling(dp, skip_updates=True)

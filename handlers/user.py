from help_for_bot import dp, bot 
from aiogram import types , Dispatcher
from sql import sql

async def welcome(message: types.Message):
    await sql.add_user(message.from_user.id)

    await message.reply(f'Привет , это бот с запясями расходов . Команды : /opinion , /expens , /earn')

async def opinion(message: types.Message):
    
    records = await sql.opinion_sql(message.from_user.id)
    
    if(len(records)):
        answer = f"История операций: \n\n"

        for r in records:
            answer += ("Расход" if r[3]== '-' else "Доход")
            answer += f" - {r[4]}"
            answer += f" ({r[2]})\n"

        await message.reply(answer)
    
    else:
        await message.reply("Записей не обнаружено!")


async def earn(message: types.Message):
    
    e = message.text
    world_list = e.split()
    value = []

    for word in world_list:
        if word.isnumeric():
            value.append(int(word))
    
    if len(value) != 0:
        for i in value:
            await sql.sql_earn(message.from_user.id, i)

        await bot.send_message(message.from_user.id , 'Доход добавлен')
    
    else:
        await bot.send_message(message.from_user.id,'Не введена сумма!')

async def expenses(message: types.Message):
    
    e = message.text
    world_list = e.split()
    value = []

    for word in world_list:
        if word.isnumeric():
            value.append(int(word))
    
    if len(value) != 0:
        for i in value:
            await sql.sql_expens(message.from_user.id, i)
    
        await bot.send_message(message.from_user.id , 'Расход добавлен')
    
    else:
        await bot.send_message(message.from_user.id,'Не введена сумма!')

def handlers_client(dp: Dispatcher):
    dp.register_message_handler(welcome , commands=['start'])
    
    dp.register_message_handler(expenses , commands=['expens'])
    
    dp.register_message_handler(earn , commands=['earn'])
    
    dp.register_message_handler(opinion , commands=['opinion'])

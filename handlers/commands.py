from loader import dp
from aiogram.types import Message
from bot_config import messages
from keyborads.actions import services, channel_link, links_btn
from aiogram.utils.markdown import text


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer_photo(photo=open('data/photos/main.jpg', 'rb'), caption=messages.start1,
                               reply_markup=channel_link)
    await message.answer(text(messages.start2), reply_markup=services)


@dp.message_handler(commands=['help'])
async def help(message: Message):
    await message.answer(text('/start - посмотреть ифнормацию о боте',
                              '\n/services - посмотреть услуги',
                              '\n/links - посмотреть ссылки для связи'))


@dp.message_handler(commands=['services'])
async def serv(message: Message):
    await message.answer(text("Список услуг:"), reply_markup=services)


@dp.message_handler(commands=['links'])
async def links(message: Message):
    await message.answer(text("Связатья со мной можно через:"), reply_markup=links_btn)

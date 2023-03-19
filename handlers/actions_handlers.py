from loader import dp, bot
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery
from aiogram.utils.markdown import text
from bot_config import messages
from bot_config.payments import PHOTO_URLS, PRICES_L
from keyborads.actions import predictions, back_button, services, back_b
from aiogram.types.message import ContentType
from data.config import PAYMENT_TOKEN


# @dp.callback_query_handler(text_contains='action_1')
# async def action_1(call: CallbackQuery):
#     await call.message.delete()
#     await call.message.answer(messages.act_1)
#
#     await bot.send_invoice(call.message.chat.id,
#                            title='title',
#                            description='description',
#                            provider_token=PAYMENT_TOKEN,
#                            currency='rub',
#                            photo_url=PHOTO_URLS[0],
#                            photo_height=512,
#                            photo_width=512,
#                            photo_size=512,
#                            prices=[PRICES[0]],
#                            start_parameter='example',
#                            payload='invoice',
#                            need_email=False,
#                            need_phone_number=False)
#
#     await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_01')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[0][0] + "\n" + messages.act_1 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[0][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_2')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[1][0] + "\n" + messages.act_2 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[1][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_3')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[2][0] + "\n" + messages.act_3 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[2][1]}</b>" + "\n" + f"Стоимость услуги:  <b>12000</b> (с прогнозом на год по теме запроса)"),
        reply_markup=back_button)
    # await call.message.answer_video(video='', )
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_4')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    # await call.message.answer_photo(photo=open('data/photos/karma.jpg', 'rb'), caption=text(
    #     PRICES_L[3][0] + "\n" + f"Стоимость услуги:  <b>{PRICES_L[3][1]}</b>" + "\n" + messages.act_4))
    await call.message.answer(
        text(PRICES_L[3][0] + "\n" + messages.act_4 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[3][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_5')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[4][0] + "\n" + messages.act_5 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[4][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_6')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[5][0] + "\n" + messages.act_6 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[5][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_7')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[6][0] + "\n" + messages.act_7 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[6][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_8')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[7][0] + "\n" + messages.act_8 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[7][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_9')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text("Прогнозирование"), reply_markup=predictions)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='action_10')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[8][0] + "\n" + messages.act_10 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[8][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='predict_1')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[9][0] + "\n" + messages.act_9_1 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[9][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.callback_query_handler(text_contains='predict_2')
async def action_1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(
        text(PRICES_L[10][0] + "\n" + messages.act_9_2 + "\n" + f"Стоимость услуги:  <b>{PRICES_L[10][1]}</b>"),
        reply_markup=back_button)
    await bot.answer_callback_query(call.id)


@dp.pre_checkout_query_handler(lambda q: True)
async def run_payload(pre_checkout_query: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: Message):
    await bot.send_message(message.chat.id, 'success')


@dp.callback_query_handler(text_contains='back')
async def back_action(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text("Список услуг:"), reply_markup=services)


# @dp.callback_query_handler(text_contains='make_order')
# async def make_order(call: CallbackQuery):
#     #await call.message.delete()
#     #await call.message.answer(text("Напишите мне: \n @Ya_Natulya_Lion"), reply_markup=back_b)

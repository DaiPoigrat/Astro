from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

services = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Анализ натальной карты (без времени рождения)', callback_data='action_01')
        ],
        [
            InlineKeyboardButton(text='Ядро личности. Анализ натальной карты Lite', callback_data='action_2')
        ],
        [
            InlineKeyboardButton(text='Полный анализ натальной карты', callback_data='action_3')
        ],
        [
            InlineKeyboardButton(text='Кармические истории', callback_data='action_4')
        ],
        [
            InlineKeyboardButton(text='Заведи деньги. Финансовая емкость', callback_data='action_5')
        ],
        [
            InlineKeyboardButton(text='Внутренняя женщина. Партнерство', callback_data='action_6')
        ],
        [
            InlineKeyboardButton(text='Сам себе враг', callback_data='action_7')
        ],
        [
            InlineKeyboardButton(text='Как перейти из позиции ребенка в позицию взрослого', callback_data='action_8')
        ],
        [
            InlineKeyboardButton(text='Прогнозирование (к чему готовиться)', callback_data='action_9')
        ],
        [
            InlineKeyboardButton(text='Ректификация (установление времени рождения)', callback_data='action_10')
        ],
        [
            InlineKeyboardButton(text='Сделать заказ', callback_data='make_order', url='https://t.me/Ya_Natulya_Lion')
        ],
    ]
)

predictions = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Солярный прогноз', callback_data='predict_1')
        ],
        [
            InlineKeyboardButton(text='Прогноз на полгода', callback_data='predict_2')
        ],
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ]
    ]
)

back_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ],
        [
            InlineKeyboardButton(text='Сделать заказ', callback_data='make_order', url='https://t.me/Ya_Natulya_Lion')
        ],
    ]
)

back_b = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Назад', callback_data='back')
        ],
    ]
)

channel_link = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Перейти в канал', callback_data='channel_link', url='https://t.me/astrosistemauspeha')
        ]
    ]
)

links_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Telegram', callback_data='tg_link', url='https://t.me/Ya_Natulya_Lion'),
        ],
        [
            InlineKeyboardButton(text='WhatsApp', callback_data='wp_link', url='https://api.whatsapp.com/send?phone=79173046633'),
            # InlineKeyboardButton(text='Viber', callback_data='vb_link', url='viber://chat?number=%2B79173046633')
        ],
    ]
)

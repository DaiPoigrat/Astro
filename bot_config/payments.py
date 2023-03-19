from aiogram.types import LabeledPrice

PRICES = [
    LabeledPrice(label='Анализ натальной карты (без времени рождения)', amount=3500),
    LabeledPrice(label='Ядро личности. Анализ натальной карты Lite', amount=5000),
    LabeledPrice(label='Полный анализ натальной карты', amount=12000),
    LabeledPrice(label='Кармические истории', amount=3000),
    LabeledPrice(label='Заведи деньги. Финансовая емкость', amount=3000),
    LabeledPrice(label='Внутренняя женщина. Партнерство', amount=2500),
    LabeledPrice(label='Сам себе враг', amount=3000),
    LabeledPrice(label='Как перейти из позиции ребенка в позицию взрослого', amount=1500),
    # LabeledPrice(label='Прогнозирование (к чему готовиться)', amount=1200),
    LabeledPrice(label='Ректификация (установление времени рождения)', amount=3500),
    LabeledPrice(label='Солярный прогноз', amount=4000),
    LabeledPrice(label='Прогноз на полгода', amount=1200),
]

PRICES_L = [
    ('Анализ натальной карты (без времени рождения)', 3500),
    ('Ядро личности. Анализ натальной карты Lite', 5000),
    ('Полный анализ натальной карты', 8000),
    ('Кармические истории', 3000),
    ('Заведи деньги. Финансовая емкость', 3000),
    ('Внутренняя женщина. Партнерство', 2500),
    ('Сам себе враг', 3000),
    ('Как перейти из позиции ребенка в позицию взрослого', 1500),
    # LabeledPrice(label='Прогнозирование (к чему готовиться)', amount=1200),
    ('Ректификация (установление времени рождения)', 3500),
    ('Солярный прогноз', 4000),
    ('Прогноз на полгода', 1200),
]

PHOTO_URLS = [
    'https://mimigram.ru/wp-content/uploads/2020/07/%D0%A7%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-%D1%84%D0%BE%D1%82%D0%BE.jpeg',
    'http://www.rosphoto.com/images/u/articles/1510/7_5.jpg',
    'https://static-cse.canva.com/blob/847064/29.jpg',
    'https://i.pinimg.com/736x/b3/a6/32/b3a632a5547d22c553075514add449db.jpg',
    'https://www.interfax.ru/ftproot/photos/photostory/2022/04/29/week/week7_1100.jpg',
    'data:image/jpeg;base64,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',
    'http://www.rosphoto.com/images/u/articles/1510/4_8.jpg'
]

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

# Создаем объекты инлайн-кнопок
from aiogram.utils.keyboard import InlineKeyboardBuilder

url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Курс "Телеграм-боты на Python и AIOgram"',
    url='https://stepik.org/120924')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Документация Telegram Bot API',
    url='https://core.telegram.org/bots/api')

# Создаем объекты инлайн-кнопок

# Создаем инлайн-кнопки с текстом, который будет отображаться на кнопке, и текстом в callback_data, который будет приходить в апдейте типа CallbackQuery в поле data.
# Создаем объект инлайн-клавиатуры и добавляем в него массив массивов кнопок (параметр inline_keyboard)
# Отправляем инлайн-клавиатуру, вместе с текстом сообщения, пользователю
# Методом callback_query у диспетчера (роутера) ловим апдейт типа CallbackQuery, отфильтровываем его по полю data и направляем в соответствующий хэндлер
# В хэндлере либо модифицируем сообщение (текст и/или кнопки), либо отправляем пустой ответ callback.answer(), чтобы у пользователя не было ощущения, что бот завис в задумчивости
# Повторяем сначала - столько раз, сколько необходимо

big_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed')

big_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed')

# Создаем объект инлайн-клавиатуры
in_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2],
                     [big_button_1],
                     [big_button_2],
                     ])



LEXICON: dict[str, str] = {
    'but_1': 'Кнопка 1',
    'but_2': 'Кнопка 2',
    'but_3': 'Кнопка 3',
    'but_4': 'Кнопка 4',
    'but_5': 'Кнопка 5',
    'but_6': 'Кнопка 6',
    'but_7': 'Кнопка 7',}

BUTTONS: dict[str, str] = {
    'btn_1': '1',
    'btn_2': '2',
    'btn_3': '3',
    'btn_4': '4',
    'btn_5': '5',
    'btn_6': '6',
    'btn_7': '7',
    'btn_8': '8',
    'btn_9': '9',
    'btn_10': '10',
    'btn_11': '11'}

# Функция для формирования инлайн-клавиатуры на лету
def create_inline_kb(width: int,
                     *args: str,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()
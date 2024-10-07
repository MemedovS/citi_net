# from aiogram import Router, types, Bot
# from aiogram.filters import Command
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.exceptions import TelegramAPIError
# from siti_bot.user_steps_manager import create_keyboard, save_step, get_previous_step
#
# router = Router()
# # Глобальная переменная для хранения состояния
# user_data = {}
# user_message_ids = {}
#
#
# async def delete_previous_message(bot: Bot, chat_id: int, message_id: int):
#     try:
#         await bot.delete_message(chat_id=chat_id, message_id=message_id)
#     except TelegramAPIError as e:
#         print(f"Ошибка при удалении сообщения: {e}")
#
#
# @router.message(lambda message: message.photo)
# async def get_image_id(message: types.Message):
#     file_id = message.photo[-1].file_id
#     await message.answer(f"file_id изображения: {file_id}")
#
#
# @router.callback_query(lambda c: c.data == "go_back")
# async def go_back(callback: types.CallbackQuery, bot: Bot):
#     user_id = callback.from_user.id
#     previous_step = get_previous_step(user_id)
#
#     if previous_step:
#         handler = STEP_HANDLERS.get(previous_step)
#         if handler:
#             if previous_step == "start":
#                 await handler(callback.message, bot)
#             else:
#                 await handler(callback, bot)
#         else:
#             await callback.answer("Не удалось определить предыдущий шаг.")
#     else:
#         await callback.answer("Нет доступных шагов для возврата.")
#
#
# async def send_welcome_message(bot: Bot, chat_id, username):
#     photo_file_id = 'AgACAgIAAxkBAAIJi2b_bm6v_PuBIT3Yo4CBzpVhPRazAAKp5TEbbC34S7rhAAGFjdT5AwEAAwIAA3gAAzYE'
#
#     try:
#         photo_message = await bot.send_photo(chat_id=chat_id, photo=photo_file_id)
#     except TelegramAPIError as e:
#         print(f"Ошибка при отправке фото: {e}")
#         photo_message = None
#
#     markup = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="🚀 Internet qoşulma 🚀", callback_data="internet_qoşulma")],
#         [InlineKeyboardButton(text="💼 Tariflər", callback_data="Tariflər")],
#         [InlineKeyboardButton(text="🟢 Bizimlə əlaqə", callback_data="Bizimlə_əlaqə")]
#     ])
#
#     welcome_message = f"🌟*{username}*🌟 sizi internetə qoşulma portalı salamlayır !"
#     welcome_message_sent = await bot.send_message(chat_id=chat_id, text=welcome_message, reply_markup=markup,
#                                                   parse_mode="Markdown")
#     return photo_message.message_id if photo_message else None, welcome_message_sent.message_id
#
#
# @router.message(Command("start"))
# async def handle_start_command(message: types.Message, bot: Bot):
#     save_step(message.from_user.id, "start")
#     await send_welcome_message(bot, message.chat.id, message.from_user.username)
#
#
# @router.callback_query(lambda c: c.data == "internet_qoşulma")
# async def internet_problems(callback: types.CallbackQuery, bot: Bot):
#     save_step(callback.from_user.id, "internet_qoşulma")
#
#     buttons = [
#         InlineKeyboardButton(text="Kampaniyalar", callback_data="Kampaniyalar"),
#         InlineKeyboardButton(text="Onlayn qeydiyat", callback_data="Onlayn_qeydiyat"),
#         InlineKeyboardButton(text="Qeriyə", callback_data="go_back")
#     ]
#     keyboard = create_keyboard(buttons)
#     await callback.message.edit_text(
#         "<b>✅CityNet-i seçmək üçün səbəblər\n✅Yüksək surət\n✅Əvəzolunmaz xidmət</b>",
#         reply_markup=keyboard, parse_mode="HTML"
#     )
#     await callback.answer()

#
# from aiogram import Router, types, Bot
# from aiogram.filters import Command
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.exceptions import TelegramAPIError
# from siti_bot.user_steps_manager import create_keyboard, save_step, get_previous_step
#
# router = Router()
# ADMIN_ID = '5760671972'
# # Глобальная переменная для хранения состояния
# user_data = {}
# user_message_ids = {}





from aiogram.exceptions import TelegramAPIError
from siti_bot.user_steps_manager import create_keyboard, save_step, get_previous_step
from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


router = Router()
ADMIN_ID = '5760671972'

# Глобальная переменная для хранения состояния
user_data = {}
user_message_ids = {}

class Form(StatesGroup):
    waiting_for_message = State()
###
async def delete_previous_message(bot: Bot, chat_id: int, message_id: int):
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
    except TelegramAPIError as e:
        print(f"Ошибка при удалении сообщения: {e}")

@router.callback_query(lambda c: c.data == "go_back")
async def go_back(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    previous_step = get_previous_step(user_id)

    if previous_step:
        handler = STEP_HANDLERS.get(previous_step)
        if handler:
            if previous_step == "start":
                await handler(callback.message, bot)
            else:
                await handler(callback, bot)
        else:
            await callback.answer("Не удалось определить предыдущий шаг.")
    else:
        await callback.answer("Нет доступных шагов для возврата.")

@router.message(lambda message: message.photo)
async def get_image_id(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"file_id изображения: {file_id}")

async def send_welcome_message(bot: Bot, chat_id, username):
    photo_file_id = 'AgACAgIAAxkBAAIMR2cBTnexZRLcEq_1SF9E-UdutvNzAAKw5DEbqhgJSDLy6t4VdYXuAQADAgADeQADNgQ'

    try:
        photo_message = await bot.send_photo(chat_id=chat_id, photo=photo_file_id)
    except TelegramAPIError as e:
        print(f"Ошибка при отправке фото: {e}")
        photo_message = None

    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Internet qoşulma 🚀", callback_data="internet_qoşulma")],
        [InlineKeyboardButton(text="💼 Tariflər", callback_data="Tariflər")],
        [InlineKeyboardButton(text="🟢 Bizimlə əlaqə", callback_data="Bizimlə_əlaqə")]
    ])

    welcome_message = f"🌟*{username}*🌟 sizi internetə qoşulma portalı salamlayır !"
    welcome_message_sent = await bot.send_message(chat_id=chat_id, text=welcome_message, reply_markup=markup,
                                                  parse_mode="Markdown")
    return photo_message.message_id if photo_message else None, welcome_message_sent.message_id

@router.message(Command("start"))
async def handle_start_command(message: types.Message, bot: Bot):
    save_step(message.from_user.id, "start")
    await send_welcome_message(bot, message.chat.id, message.from_user.username)


@router.callback_query(lambda c: c.data == "internet_qoşulma")
async def internet_problems(callback: types.CallbackQuery, bot: Bot):
    save_step(callback.from_user.id, "internet_qoşulma")

    buttons = [
        InlineKeyboardButton(text="Kampaniyalar", callback_data="Kampaniyalar"),
        InlineKeyboardButton(text="Onlayn qeydiyat", callback_data="Onlayn_qeydiyat"),
        InlineKeyboardButton(text="Qeriyə", callback_data="go_back"),
        InlineKeyboardButton(text="🔙 Əsas menyu", callback_data="go_home")
    ]
    keyboard = create_keyboard(buttons)
    photo_file_id = 'AgACAgIAAxkBAAIKbWb_lhpm7rTsB_W1xWUh65gMMbAtAAIH3zEbqhj5S6KWPEAwcpM_AQADAgADeAADNgQ'
    caption_text = (
        "<b>✅Həm müasir, həm də pulsuz cihazlar təqdim edirik! \nQoşulma zamanı tarifə uyğun olaraq bir ayın ödənişini etdikdə\n"
        "yeni nəsil Wi-Fi ruter və TV-box sizə pulsuz təqdim olunacaq.\nCityNet abunəçisi olduğunuz müddətdə cihazlar ödənişsizdir.</b>")

    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=photo_file_id,
        caption=caption_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )
    await callback.answer()


@router.callback_query(lambda c: c.data == "go_home")
async def go_home(callback: types.CallbackQuery, bot: Bot):
    user_id = callback.from_user.id
    # Сбрасываем шаги пользователя
    save_step(user_id, "start")
    # Отправляем начальное сообщение
    await send_welcome_message(bot, callback.message.chat.id, callback.from_user.username)
    await callback.answer()


@router.callback_query(lambda c: c.data == "Kampaniyalar")
async def internet_Kampaniyalar(callback: types.CallbackQuery, bot: Bot):
    save_step(callback.from_user.id, "Kampaniyalar")
    buttons = [
        InlineKeyboardButton(text="Bir + Bir", callback_data="bir_bir"),
        InlineKeyboardButton(text="Pulsuz cihazlar", callback_data="pulsuz_cihazlar"),
        InlineKeyboardButton(text="Ulduzumla CityNetdən 50% endirim!", callback_data="endirim_citynet"),
        InlineKeyboardButton(text="Onlayn qeydiyat", callback_data="Onlayn_qeydiyat"),
        InlineKeyboardButton(text="Qeriyə", callback_data="go_back"),
        InlineKeyboardButton(text="🔙 Əsas menyu", callback_data="go_home")
    ]
    keyboard = create_keyboard(buttons)
    photo_file_id = 'AgACAgIAAxkBAAIKdGb_lmC6G_wNFkoBAAFFQNeNYlXBeAACCt8xG6oY-UsZn1J16rN27QEAAwIAA3gAAzYE'
    caption_text = (
        "<b>✅Kampaniyalar \nMövcud kampaniyalarla burada tanış ola bilərsiniz.\n</b>")
    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=photo_file_id,
        caption=caption_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )

    await callback.answer()




@router.callback_query(lambda c: c.data == "Onlayn_qeydiyat")
async def online_registration(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    save_step(user_id, "Onlayn_qeydiyat")

    await callback.message.answer("📞 <b>Salam! Zəhmət olmasa,telefon nömrasini qeyd edin:</b>", parse_mode="HTML")
    user_data[user_id] = {"phone1": None}  # Инициализируем данные пользователя

    await callback.answer()


@router.message(lambda message: message.from_user.id in user_data and user_data[message.from_user.id]["phone1"] is None)
async def process_first_phone(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["phone1"] = message.text  # Сохраняем первый телефонный номер

    await message.answer("📞 <b>Zəhmət olmasa, ikinci telefon nömrasini qeyd edin:</b>", parse_mode="HTML")
    user_data[user_id]["phone2"] = None  # Инициализируем второй номер как None


@router.message(lambda message: message.from_user.id in user_data and user_data[message.from_user.id]["phone2"] is None)
async def process_second_phone(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id]["phone2"] = message.text  # Сохраняем второй телефонный номер

    await message.answer("🏠 <b>Zəhmət olmasa, ünvanı qeyd edin:</b>", parse_mode="HTML")
    user_data[user_id]["address"] = None  # Инициализируем адрес как None


@router.message(
    lambda message: message.from_user.id in user_data and user_data[message.from_user.id]["address"] is None)
async def process_address(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    user_data[user_id]["address"] = message.text  # Сохраняем адрес

    await message.answer("📝<b> Zəhmət olmasa, ad soyad ata adını yazın (FİO):</b>", parse_mode="HTML")
    user_data[user_id]["full_name"] = None  # Инициализируем ФИО как None


@router.message(
    lambda message: message.from_user.id in user_data and user_data[message.from_user.id]["full_name"] is None)
async def process_full_name(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    user_data[user_id]["full_name"] = message.text  # Сохраняем полное имя

    await message.answer("💼<b> Zəhmət olmasa, tarifi secəsin:\n🟢 Tarif 25 ₼\n🟢 Tarif 31 ₼\n🟢 Tarif 33₼</b>",
                         parse_mode="HTML")
    user_data[user_id]["tariff"] = None  # Инициализируем тариф как None


@router.message(lambda message: message.from_user.id in user_data and user_data[message.from_user.id]["tariff"] is None)
async def process_tariff(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    user_data[user_id]["tariff"] = message.text  # Сохраняем тариф

    # Отправляем данные администратору
    admin_chat_id = ADMIN_ID  # Замените на ID вашего администратора
    phone1 = user_data[user_id]["phone1"]
    phone2 = user_data[user_id]["phone2"]
    address = user_data[user_id]["address"]
    full_name = user_data[user_id]["full_name"]
    tariff = user_data[user_id]["tariff"]

    await bot.send_message(
        chat_id=admin_chat_id,
        text=f"<b>📝 Yeni sorğu:\n"
             f"👤FİO: {full_name}\n"
             f"📞Telefon 1: {phone1}\n"
             f"📞Telefon 2: {phone2}\n"
             f"🏠Ünvan: {address}\n"
             f"💼Tarif: {tariff}</b>", parse_mode="HTML"
    )

    await message.answer("🔔 <b>Təşəkkürlər! Sizin sorğunuz qeydə alındı.</b>", parse_mode="HTML")
    del user_data[user_id]  # Удаляем данные пользователя после завершения процесса

@router.callback_query(lambda c: c.data == "bir_bir")
async def internet_bir_bir(callback: types.CallbackQuery, bot: Bot):
    save_step(callback.from_user.id, "bir_bir")

    buttons = [
        InlineKeyboardButton(text="Onlayn qeydiyat", callback_data="Onlayn_qeydiyat"),
        InlineKeyboardButton(text="Qeriyə", callback_data="go_back"),
        InlineKeyboardButton(text="🔙 Əsas menyu", callback_data="go_home")
    ]
    keyboard = create_keyboard(buttons)
    photo_file_id = 'AgACAgIAAxkBAAII5Gb-tRoOSw-jYVZaHzl1cSkEbFg_AALS4jEbbC34S29XRv8Z4p8bAQADAgADbQADNgQ'
    caption_text = ("<b>✅Artıq CityNet xidmətlərinə yeni qoşulan \nvə mövcud tariflərdən birini seçən müştərilər \n"
                    "pulsuz router, modem  əldə edə bilərlər.</b>")

    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=photo_file_id,
        caption=caption_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "endirim_citynet")
async def internet_endirim_citynet(callback: types.CallbackQuery, bot: Bot):
    save_step(callback.from_user.id, "endirim_citynet")

    buttons = [
        InlineKeyboardButton(text="Onlayn qeydiyat", callback_data="Onlayn_qeydiyat"),
        InlineKeyboardButton(text="Qeriyə", callback_data="go_back"),
        InlineKeyboardButton(text="🔙 Əsas menyu", callback_data="go_home")
    ]
    keyboard = create_keyboard(buttons)

    photo_file_id = 'AgACAgIAAxkBAAII52b-tUV0vP4p8ECLCj88C_7jB-yyAALT4jEbbC34S5nWjnp5cG-xAQADAgADbQADNgQ'
    caption_text = ("<b>✅Mövcud müştərilərimiz \nvə yeni müştərilər \n"
                    "Ulduzumla CityNetdən 50% endirim!</b>")
    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=photo_file_id,
        caption=caption_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )

    await callback.answer()


@router.callback_query(lambda c: c.data == "pulsuz_cihazlar")
async def internet_pulsuz_cihazlar(callback: types.CallbackQuery, bot: Bot):
    save_step(callback.from_user.id, "pulsuz_cihazlar")  # Сохраняем шаг

    # Кнопки для клавиатуры
    buttons = [
        InlineKeyboardButton(text="Onlayn qeydiyat", callback_data="Onlayn_qeydiyat"),
        InlineKeyboardButton(text="Qeriyə", callback_data="go_back") , # Кнопка "Назад"
        InlineKeyboardButton(text="🔙 Əsas menyu", callback_data="go_home")
    ]
    keyboard = create_keyboard(buttons)

    # Идентификатор файла фотографии или URL
    photo_file_id = 'AgACAgIAAxkBAAIHhmb-TAnsryTcAeDhmrXhYN4GnoFoAAK03jEbbC3wS2JHBL_layfYAQADAgADeQADNgQ'  # Замените на ваш file_id или URL

    # Текст для подписи к фото
    caption_text = (
        "<b>✅Həm müasir, həm də pulsuz cihazlar təqdim edirik! \nQoşulma zamanı tarifə uyğun olaraq bir ayın ödənişini etdikdə\n"
        "yeni nəsil Wi-Fi ruter və TV-box sizə pulsuz təqdim olunacaq.\nCityNet abunəçisi olduğunuz müddətdə cihazlar ödənişsizdir.</b>")

    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=photo_file_id,
        caption=caption_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


@router.callback_query(lambda c: c.data == "Tariflər")
async def issue_exists(callback: types.CallbackQuery, bot: Bot):
    save_step(callback.from_user.id, "Tariflər")  # Сохраняем шаг

    buttons = [
        InlineKeyboardButton(text="Onlayn qeydiyat", callback_data="Onlayn_qeydiyat"),
        InlineKeyboardButton(text="Qeriyə", callback_data="go_back"),
        InlineKeyboardButton(text="🔙 Əsas menyu", callback_data="go_home")

    ]
    keyboard = create_keyboard(buttons)
    # Идентификатор файла фотографии или URL
    photo_file_id = 'AgACAgIAAxkBAAIMOmcBR_POjhKBrH2ulp9J9yW296jrAAJq5DEbqhgJSKZCV7JxIb37AQADAgADeQADNgQ'  # Замените на ваш file_id или URL

    # Текст для подписи к фото
    caption_text = (
        "<b>✅Həm müasir, həm də pulsuz cihazlar təqdim edirik! \nQoşulma zamanı tarifə uyğun olaraq bir ayın ödənişini etdikdə\n"
        "yeni nəsil Wi-Fi ruter və TV-box sizə pulsuz təqdim olunacaq.\nCityNet abunəçisi olduğunuz müddətdə cihazlar ödənişsizdir.</b>")

    await bot.send_photo(
        chat_id=callback.from_user.id,
        photo=photo_file_id,
        caption=caption_text,
        reply_markup=keyboard,
        parse_mode="HTML"
    )




# Обработчик кнопки "Bizimlə_əlaqə"
@router.callback_query(lambda c: c.data == "Bizimlə_əlaqə")
async def contact_admin(callback: types.CallbackQuery, state: FSMContext,bot: Bot):
    await callback.message.answer("<b>❗️📝Siz mesajınızı yaza bilərsiniz:\n📞+994503275452</b>",parse_mode="HTML")

    # Переходите к состоянию ожидания сообщения
    await state.set_state(Form.waiting_for_message)

# Обработчик сообщений в состоянии ожидания
@router.message()  # Убираем 'state' из декоратора
async def handle_message(message: types.Message, state: FSMContext,bot: Bot):
    # Проверяем, что пользователь находится в нужном состоянии
    current_state = await state.get_state()
    if current_state == Form.waiting_for_message.state:
        # Отправьте сообщение админу
        await bot.send_message(ADMIN_ID, f"<b>✅Yeni mesaj:\n\n{message.text}</b>", parse_mode="HTML")

        await message.answer("<b>✅Mesajınız göndərildi!</b>", parse_mode="HTML")

        # Очистить состояние (сбросить состояние)
        await state.clear()











# Регистрация обработчиков шагов
STEP_HANDLERS = {
    "start": handle_start_command,
    "internet_qoşulma": internet_problems,
    "Tariflər": issue_exists,
    "Kampaniyalar": internet_Kampaniyalar,
    "bir_bir": internet_bir_bir,
    "pulsuz_cihazlar": internet_pulsuz_cihazlar,
    "endirim_citynet": internet_endirim_citynet,
}

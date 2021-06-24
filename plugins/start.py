from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Support Channel", url="https://t.me/Cat_Telegram_Projects")],
        [InlineKeyboardButton(
            "Support Group", url="https://t.me/Cat_Telegram_Project_Club")]
    ])
    welcomed = f"Hey! <b>{message.from_user.first_name}</b>\nI am A powerfull Youtube Downloader Telegram Bot Created by @Cat_of_TelegramX. Use ```/help``` to see My potential...Join Support Group If you have Any doubts."
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

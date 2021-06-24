from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"__I am A powerful Youtube Downloader Telegram Bot Powered by Cat. Send me link of Youtube i can Download in Many Formats...Powered by Youtube Downloader by @Cat_of_TelegramX__"
    await message.reply_text(helptxt)

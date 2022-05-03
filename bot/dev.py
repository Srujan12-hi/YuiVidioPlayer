from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("info")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
=> Bot Devlopers
1) @Sruja_12
2) @thatfuckingsoul
3) @fake_account_srs
4) @finding_someone_here
 </b>"""

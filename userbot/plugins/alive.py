import time
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, cblacversion, get_readable_time, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "BLAC"
CAT_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "✮ MY 𝔹𝕃𝔸ℂ 2.0 𝔹𝕆𝕋 IS RUNNING SUCCESSFULLY ✮"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  ✥ " 

file1 = "https://telegra.ph/file/8002a948622a0c8618e38.jpg

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if CAT_IMG:
        cat_caption = f"{CUSTOM_ALIVE_TEXT}\n\n"
        cat_caption += f"{EMOJI} Database : {check_sgnirts}\n"
        cat_caption += f"{EMOJI} Telethon version : {version.version}\n"
        cat_caption += f"{EMOJI} B-lac Version : {blacversion}\n"
        cat_caption += f"{EMOJI} Python Version : {python_version()}\n"
        cat_caption += f"{EMOJI} Uptime : {uptime}\n"
        cat_caption += f"{EMOJI} Master: {mention}\n"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=blac_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"{CUSTOM_ALIVE_TEXT}\n\n"
            f"{EMOJI} Database : {check_sgnirts}\n"
            f"{EMOJI} Telethon Version : {version.version}\n"
            f"{EMOJI} Blac Version : {catversion}\n"
            f"{EMOJI} Python Version : {python_version()}\n"
            f"{EMOJI} Uptime : {uptime}\n"
            f"{EMOJI} Master: {mention}\n",
        )


@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    reply_to_id = await reply_id(alive)
    cat_caption = f"Blac is Up and Running\n"
    cat_caption += f"  -Telethon version : {version.version}\n"
    cat_caption += f"  -Catuserbot Version : {catversion}\n"
    cat_caption += f"  -Python Version : {python_version()}\n"
    cat_caption += f"  -Master: {mention}\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "Plugin : alive\
      \n\n  •  Syntax : .alive \
      \n  •  Function : status of bot will be showed\
      \n\n  •  Syntax : .ialive \
      \n  •  Function : inline status of bot will be shown.\
      \nSet ALIVE_PIC var for media in alive message"
    }
)

import time
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, cblacversion, get_readable_time, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "BLAC"
CAT_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "â® MY ğ¹ğğ¸â 2.0 ğ¹ğğ IS RUNNING SUCCESSFULLY â®"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "  â¥ " 

file1 = "https://telegra.ph/file/8002a948622a0c8618e38.jpg"

@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    pm_caption = "**ğ¹ğğ¸â 2.0 ğğ ğâğğâğ¼**\n\n"
    
    pm_caption += f"ğ¹ğğ¸â 2.0ğ§¿: {Blacversion}\n"
    
    pm_caption += "ğ¨ğğ¼ğğ¼ğâğâğ¨: 1.19.0 \n"
    
    pm_caption += f"ğ$ááªOğ: {sudou}\n"
    
    pm_caption += "ğââğ¸ââğ¼ğğ: [ğğğâ](https://t.me/BLACUSERBOT_SUPPORT1)\n"
    
    pm_caption += "ğ ï¸ââğ¼ğ¸ğğâğ ï¸: [âğğğ¹ âğ¼âğ¼](https://t.me/ERROR_404_USER_NOT_FOUNDED)\n\n"
    
    pm_caption += "ğğ¹ğğ¸â ğ¾ğ¸âğ¾ ğğâğ¼âğ: [ğğ¸ğğğ¸ ğğ¸ğğ](https://t.me/JATTGAMINGYT11)\n\n"
    
    pm_caption += "    [ğ¸áEá­Oğ¸](https://github.com/B-Lac/BLAC-2.0-USERBOT) ğ¹ [ğğğâğ¼âğğ¼ğ](https://github.com/B-Lac/BLAC-2.0-USERBOT/blob/master/LICENSE)\n"
    
    pm_caption += f"â¾ ğğ ğğ¸ğğğ¼â â¤ï¸ â [{DEFAULTUSER}](tg://user?id={ghanti})\n\n"
    pm_caption += (
        "[ğ¹ ğğ¸â ğ¹ğğ ğâ ğ½ğâğ¼  ](https://t.me/BLACUSERBOT_SUPPORT1)'

@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    reply_to_id = await reply_id(alive)
    results = await bot.inline_query(tgbotusername, pm_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# à´µà´¿à´µà´°à´£à´ à´à´à´¿à´àµà´àµà´®à´¾à´±àµà´±à´¿à´àµà´àµà´£àµà´àµ à´ªàµà´àµà´¨àµà´¨à´µàµ¼
# à´àµà´°àµà´¡à´¿à´±àµà´±àµ à´µàµà´àµà´à´¾àµ½ à´¸à´¨àµà´¤àµà´·à´®àµ à´à´³àµà´³àµ..!
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
        output = f"â {str(e)}"
        is_database_working = False
    else:
        output = "Functioning Normally"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "Plugin : alive\
      \n\n  â¢  Syntax : .alive \
      \n  â¢  Function : status of bot will be showed\
      \n\n  â¢  Syntax : .ialive \
      \n  â¢  Function : inline status of bot will be shown.\
      \nSet ALIVE_PIC var for media in alive message"
    }
)

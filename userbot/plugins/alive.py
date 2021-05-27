# Thanks to Sipak bro and Aryan..
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# modified by Pawan jatt
# Kang with credits else gay...
import asyncio
import os
from io import BytesIO

import requests
from PIL import Image

from userbot import ALIVE_NAME
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd, sudo_cmd

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else " B乛LAC Uʂҽɾზσƚ"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO", None)
Blacversion = "1.5"
ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

Jatt = bot.uid
# Thanks to Sipak bro and Raganork..
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/8002a948622a0c8618e38.jpg"

""" =======================CONSTANTS====================== """
pm_caption = "𝔹𝕃𝔸ℂ 2.0 𝕀𝕊 𝕆ℕ𝕃𝕀ℕ𝔼\n\n"

pm_caption += f"𝔹𝕃𝔸ℂ 2.0🧿: {Blacversion}\n"

pm_caption += "🔨𝕋𝔼𝕃𝔼𝕋ℍ𝕆ℕ🔨: 1.19.0 \n"

pm_caption += f"🙋$ᑌᗪO🙋: {sudou}\n"

pm_caption += "🔗ℂℍ𝔸ℕℕ𝔼𝕃🔗: 𝕁𝕆𝕀ℕ\n"

pm_caption += "🛠️ℂℝ𝔼𝔸𝕋𝕆ℝ🛠️: ℕ𝕆𝕆𝔹 ℍ𝔼ℝ𝔼\n\n"

pm_caption += "👑𝔹𝕃𝔸ℂ 𝔾𝔸ℕ𝔾 𝕆𝕎ℕ𝔼ℝ👑: 𝕁𝔸𝕊𝕊𝔸 𝕁𝔸𝕋𝕋\n\n"

pm_caption += "    🔸ᖇEᑭO🔸 🔹 📜𝕃𝕀ℂ𝔼ℕ𝕊𝔼📜\n"

pm_caption += f"➾ 𝕄𝕐 𝕄𝔸𝕊𝕋𝔼ℝ ❤️ ☞ {DEFAULTUSER}\n\n"
pm_caption += (
    "𝔹 𝕃𝔸ℂ 𝔹𝕆𝕋 𝕆ℕ 𝔽𝕀ℝ𝔼  '


@borg.on(lightning_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def amireallyalive(yes):
    await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

# reupdate by : ramadhani892
# Thanks For @tofik_dn & @mrismanaziz

import random

from userbot import CMD_HELP, BLACKLIST_CHAT, CMD_HANDLER as cmd
from userbot.utils import ram_cmd, edit_or_reply, edit_delete
from userbot import owner
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterMusic

@ram_cmd(pattern=r"vbkp$")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_delete(
            event, "**NYARI BOKEP JANGAN DISINI ANJING LU NGENTOD!!!!!**", 5
        )
    ram = await edit_or_reply(event, "`Bentar tod lg gua ambilin...`")
    try:
        videonya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@AsupanAku", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(videonya),
            caption=f"Silahkan menikmati.",
            reply_to=event.reply_to_msg_id)
        await ram.delete()
    except Exception:
        await ram.edit("Kalo Gak bisa, Ya jangan nangis tod")



@ram_cmd(pattern=r"vtik$")
async def _(event):
    ram = await edit_or_reply(event, "`Bentar Gua cariin....`")
    try:
        videonya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tiktody", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(videonya),
            caption=f"Silahkan menikmati [{owner}](tg://user?id={aing.id})",
            reply_to=event.reply_to_msg_id)
        await ram.delete()
    except Exception:
        await ram.edit("Kalo Gak bisa, Ya jangan nangis tod")


@ram_cmd(pattern=r"ayg$")
async def _(event):
    syg = await edit_or_reply(event, "Gua Cariin Ayang yg cocok sama lu....")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tiktody", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Ini Ayang Lu [{owner}](tg://user?id={aing.id})",
            reply_to=event.reply_to_msg_id)
        await syg.delete()
    except Exception:
        await syg.edit("Kalo Gak bisa, Ya jangan nangis tod")

@ram_cmd(pattern=r"dcewe$")
async def _(event):
    dsh = await edit_or_reply(event, "**Sebentar ya cok....**")
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancewesangesange", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Silahkan menikmati tot! [{owner}](tg://user?id={aing.id})",
            reply_to=event.reply_to_msg_id)
        await dsh.delete()
    except Exception:
        await dsh.edit("`Yah Kurang beruntung lu cok...`")


@ram_cmd(pattern=r"dcowo$")
async def _(event):
    dsh = await edit_or_reply(event, "`Bentar cok...`")
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@desahancowo", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Silahkan Menikmati [{owner}](tg://user?id={aing.id})",
            reply_to=event.reply_to_msg_id)
        await dsh.delete()
    except Exception:
        await dsh.edit("`Yah Kurang Beruntung lu cok...`")
# =================≠================================================================================================================================

@ram_cmd(pattern=r"alq$")
async def _(event):
    ram = await edit_or_reply(event, "`Masya Allah, tobat.....`")
    try:
        qurannya = [
            quran
            async for quran in event.client.iter_messages(
                "@kureenkeryam", filter=InputMessagesFilterMusic
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(qurannya),
            caption=f"Dengarkan Dengan Khusyu [{owner}](tg://user?id={aing.id})",
           reply_to=event.reply_to_msg_id)
        await ram.delete()
    except Exception:
        await ram.edit(f"`Kalo Ga bisa, Jangan nangis ya {owner}`")


@ram_cmd(pattern=r"sholawat$")
async def _(event):
    ram = await edit_or_reply(event, "**Sedang mencari sholawat....**")
    try:
        sholawatnya = [
            quran
            async for quran in event.client.iter_messages(
                "@pengagum_sholawat", filter=InputMessagesFilterMusic
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(sholawatnya),
            caption=f"Dengerin tuh Sholawat Biar adem [{owner}](tg://user?id={aing.id})",
           reply_to=event.reply_to_msg_id)
        await ram.delete()
    except Exception:
        await ram.edit(f"`Kalo Gabisa Ya jangan nangis lah {owner}.`")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}vtik`\
        \n  •  **Function : **Untuk mengirim Video Asupan Dari Tiktok Secara Random.\
        \n\n  • **Syntax  :** `{cmd}vbkp`\
        \n  •  **Function : **Untuk Mengirim Video Asupan Biologi Dari Sesuatu Secara Random.\
        \n\n  •  **Syntax :** `{cmd}ayg`\
        \n  •  **Function : **Untuk Mengirim Foto cewe cantik secara random.\
        \n\n  •  **Syntax :** `{cmd}dcowo` or  `{cmd}dcewe`\
        \n  •  **Function : **Untuk Mengirim suara desah buat lu yang sange.\
    "
    }
)

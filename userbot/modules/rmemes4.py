# RAM-UBOT

import asyncio
from time import sleep


from userbot import CMD_HELP, GROUP_LINK, IG_ALIVE, REPO_NAME, owner
from userbot.utils import edit_or_reply, ram_cmd
from userbot import CMD_HANDLER as cmd


@ram_cmd(pattern="bulan$")
async def _(event):
    event = await edit_or_reply(event, "bulan.")
    animation_interval = 0.2
    animation_ttl = range(96)
    await event.edit("bulan..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


@ram_cmd(pattern="heli(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "▬▬▬.◙.▬▬▬ \n"
                     "═▂▄▄▓▄▄▂ \n"
                     "◢◤ █▀▀████▄▄▄▄◢◤ \n"
                     "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
                     "◥█████◤ \n"
                     "══╩══╩══ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ \n"
                     "╬═╬ HALO ANAK YATIM,AKU DATANG :) \n"
                     "╬═╬☻/ \n"
                     "╬═╬/▌ \n"
                     "╬═╬/ \\ \n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="tembak(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "_/﹋\\_\n"
                     "(҂`_´)\n"
                     "<,︻╦╤─ ҉\n"
                     r"_/﹋\_"
                     "\n**Mau Jadi Pacarku Gak?!**", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="bundir(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "`DIDUGA BUNDIR KARNA DI GHOSTING...`          \n　　　　　|"
                     "\n　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　　　　　| \n"
                     "　／￣￣＼| \n"
                     "＜ ´･ 　　 |＼ \n"
                     "　|　３　 | 丶＼ \n"
                     "＜ 、･　　|　　＼ \n"
                     "　＼＿＿／∪ _ ∪) \n"
                     "　　　　　 Ｕ Ｕ\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="tawa(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "────██──────▀▀▀██\n"
                     "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
                     "▄▀──█▄▄──────█─█▄▄\n"
                     "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
                     "─▀───────▀▀─▀───────▀▀\n**Awkwokwokwok Anak Ngentot..**", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="ular(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "░░░░▓\n"
                     "░░░▓▓\n"
                     "░░█▓▓█\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░░░██▓▓██\n"
                     "░░░░██▓▓██\n"
                     "░░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░██▓▓██\n"
                     "░░░██▓▓███\n"
                     "░░░░██▓▓████\n"
                     "░░░░░██▓▓█████\n"
                     "░░░░░░██▓▓██████\n"
                     "░░░░░░███▓▓███████\n"
                     "░░░░░████▓▓████████\n"
                     "░░░░█████▓▓█████████\n"
                     "░░░█████░░░█████●███\n"
                     "░░████░░░░░░░███████\n"
                     "░░███░░░░░░░░░██████\n"
                     "░░██░░░░░░░░░░░████\n"
                     "░░░░░░░░░░░░░░░░███\n"
                     "░░░░░░░░░░░░░░░░░░░\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()


@ram_cmd(pattern="ya(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
                     "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
                     "██████▄▄█‡‡‡‡‡‡████████▄\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
                     "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
                     "█████‡‡‡‡‡‡‡██████████\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="tank(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
                     "▂▄▅█████████▅▄▃▂…\n"
                     "[███████████████████]\n"
                     "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="babi(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "┈┈┏━╮╭━┓┈╭━━━━╮\n"
                     "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
                     "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
                     "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
                     "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
                     "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
                     "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
                     "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="ajg(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "╥━━━━━━━━╭━━╮━━┳\n"
                     "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
                     "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
                     "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
                     "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
                     "╨━━┗┛┗┛━━┗┛┗┛━━┻\n", reply_to=typew.reply_to_msg_id)
    await typew.delete()

@ram_cmd(pattern="gbn(?: |$)(.*)")
async def _(gbon):
    typew = await edit_or_reply(gbon, "`Kita Gban Jamet duls!!...`")
    sleep(1)
    await typew.edit("`Memulai global banned...✅`")
    sleep(2)
    await typew.edit("`Proses Global banned...✅`")
    sleep(3)
    await typew.edit(f"╭✠╼━━━━━━❖━━━━━━━✠\n┣• **TUAN:** `{owner}`\n┣• **PIBOONG:** [INSTAGRAM]({IG_ALIVE})\n┣• **Aksi:** `PROMOSI`\n╰✠╼━━━━━━❖━━━━━━━✠")

@ram_cmd(pattern="gkck(?: |$)(.*)")
async def _(gkack):
    typew = await edit_or_reply(gkack, "**Proses global kick Si ngentot!!...**")
    sleep(3)
    await typew.edit("__mengeluarkan dari (1) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (2) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (3) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (4) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (5) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (6) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (7) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (8) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (9) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (10) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (11) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (12) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (13) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (14) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (15) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (16) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (17) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (18) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (19) Group__")
    sleep(1)
    await typew.edit("__mengeluarkan dari (20) Group__")
    sleep(2)
    await typew.edit("**Pengguna berhasil di kick global dari (20) obrolan dalam grup.**")


@ram_cmd(pattern="gmt(?: |$)(.*)")
async def _(gmyut):
    typew = await edit_or_reply(gmyut, "`Memulai proses Global mute...`")
    sleep(3)
    await typew.edit("`Pengguna berhasil di Global mute...!`")


@ram_cmd(pattern="tolol(?: |$)(.*)")
async def _(tolol):
    typew = await edit_or_reply(tolol, "`TOLOL...`")
    sleep(2)
    await typew.edit("`Pertama Kamu tolol....`")
    sleep(1)
    await typew.edit("`Kedua Kamu memang tolol...`")
    sleep(1)
    await typew.edit("`Ketiga Kamu benar benar tolol..`")
    sleep(1)
    await typew.edit("`Dan kamu di lahirkan Dalam keadaan tolol...`")
    sleep(1)
    await typew.edit("`Dasar kamu anak TOLOL...`")
    sleep(1)
    await typew.edit("`T`")
    await typew.edit("`TO`")
    await typew.edit("`TOL`")
    await typew.edit("`TOLO`")
    await typew.edit("`TOLOL`")
    await typew.edit("`TOLOL!!!!`")


@ram_cmd(pattern="uasu(?: |$)(.*)")
async def _(uasuh):
    typew = await edit_or_reply(uasuh, "`Memeriksa dyno heroku anda...`")
    sleep(1)
    await typew.edit("✨")
    sleep(2)
    await typew.edit(f"𝗜𝗡𝗙𝗢 𝗞𝗘𝗞𝗨𝗔𝗧𝗔𝗡!! {REPO_NAME}\n\n"
                     "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                     "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗦𝗔𝗔𝗧 𝗜𝗡𝗜 :\n"
                     "┣• ▸ 999 ᴊᴀᴍ - 999 ᴍᴇɴɪᴛ.\n" 
                     "┣• ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : 999%\n" 
                     "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                     "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
                     "╭✠╼━━━━━━❖━━━━━━━✠╮\n"
                     "┣•𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔𝗔𝗡 𝗕𝗨𝗟𝗔𝗡 𝗜𝗡𝗜 :\n"
                     "┣• ▸ `999999` ᴊᴀᴍ - `999999` ᴍᴇɴɪᴛ.\n"
                     "┣• ▸ ᴘʀᴇꜱᴇɴᴛᴀꜱᴇ : 1000%.\n"
                     "╰✠╼━━━━━━❖━━━━━━━✠╯\n"
                     f"𝗣𝗘𝗠𝗜𝗟𝗜𝗞  : {owner}\n"
                     f"**•JOIN•** : [MY GROUP]({GROUP_LINK})")


@ram_cmd(pattern="kickme(?: |$)(.*)")
async def _(kikem):
    typew = await edit_or_reply(kikem, f"`{owner}, Saat Nya Pergi...`")
    sleep(3)
    await typew.edit(f"`{owner} Telah meninggalkan Group....`")


@ram_cmd(pattern="gi(?: |$)(.*)")
async def _(igehy):
    typew = await edit_or_reply(igehy, "**Mutualan Yukkk!...**")
    sleep(2)
    await typew.edit(f"𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌= [𝐓𝐄𝐊𝐀𝐍]({IG_ALIVE})")


@ram_cmd(pattern="fck(?: |$)(.*)")
async def _(event):
    typew = await edit_or_reply(event, ".                       /¯ )")
    await typew.edit(".                       /¯ )\n                      /¯  /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
    await typew.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")

CMD_HELP.update({
    "memes7":
    f"`{cmd}bulan` ; `{cmd}hati` ; `{cmd}gbn` ; `{cmd}tolol` ; `{cmd}gmt`\
    \nUsage: liat aja.\
    \n\n`{cmd}heli` ; `{cmd}tank` ; `{cmd}tembak`\n`{cmd}bundir`\
    \nUsage: liat sendiri."
})

CMD_HELP.update({
    "memes8":
    f".y` ; `{cmd}uasu` ; `{cmd}gkck`\
    \nUsage: jempol , Cek dyno & prank global kick\
    \n\n`{cmd}tawa` ; `{cmd}oy` ; `{cmd}fck`\
    \nUsage: ketawa lari , Nyuruh nimbrung , fvck & Coba sendiri.\
    \n\n`{cmd}ular` ; `{cmd}babi` ; `{cmd}ajg`\
    \nUsage: liat sendiri."
})

CMD_HELP.update(
    {
    "islamic":
    f"**plugin: **Islamic.\
    \n\n  • **Syntax :** `{cmd}alq`\
    \nUsage: Memberikan Voice Al-Qur'an yang menyejukan hati.\
    \n\n  • **Syntax :** `{cmd}sholawat`\
    \nUsage: Memberikan Voice Sholawat Yang membuat Tenang.\
    "
    }
)

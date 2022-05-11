#  (C) @pocongonlen
# ⚠️ Do not remove credits.

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import poci_cmd
from random import choice

KATAPOCONG = [
    "pawang? apakah itu semacam pimpinan para hewan?",
    "hidup mu saja masih berantakan, malah sok ngurusin hidup orang!",
    "bukan hidup yg sulit , tapi dirimu yg mempersulit",
    "Ulang tahun? kau hanya merayakan kematian mu semakin dekat!",
    "Jangan tanya kenapa aku berubah, liat ultraman dia berubah karena ada masalah.",
    "Percaya diri memang penting, tapi sadar diri lebih penting.",
    "**Mau di hargai , tapi tidak bisa menghargai**.",
    "healing? apakah itu kata agar orang orang peduli dengan mu?",
    "Dia sehat, tetapi tidak sholat!",
    "Dasar Baperan Itu Kata Yang Sering Dilontarkan Oleh Orang Tidak Punya Akhlak",
    "Baperan? apakah itu kata untuk berlindung setelah menghina?",
    "Pacaran? apa maksudmu berteman dengan cara aneh?",
    "Kau Butuh Healing? Saya Rasa Tidak, Yang Kau Butuhkan Hanyalah Uang",
    "Aku sudah terbiasa melakukannya sendiri! kau cukup diam dan memperhatikannya",
    "Tidak ada sahabat sejati, kecuali kita sendiri.",
    "diam seperti wibu bergerak mencintai mu",
    "Jangan menilai orang dari luar, Aqua saja bisa berisi arak!",
    "Seekor singa tak pernah mengatakan dirinya raja!",
    "Yang tinggi saja tidak melangit, ini tanah sok jadi langit!",
    "Halu adalah kebiasaan orang jelek!",
    "Kebohongan adalah hal indah bagi mereka yang tidak tau kebenaran",
    "Seperti biasa tidak ada yang berbeda hari ini.",
    "Kau Tau Namaku, Tapi Tidak Dengan Nasibku",
    "Jangan sesekali kau membohongi seorang pembohong",
    "Apakah cinta membuat mu bahagia?",
    "Sekali tanah sampai kapanpun tanah",
    "Jangan khawatir, kita lihat dulu cara dia bermain",
    "Jangan bermain-main dengan pemain",
    "Senjata hanyalah mainan yang membuat kita terlihat kuat",
    "Tanah kok melangit",
    "Gertakan mu tak se seram gertakan bapakku",
    "Dia mengajariku bermain di permainan yg sudah ku tamatkan",
    "Dia tidak mengetahui siapa yang sebenarnya",
    "Bukankah pacaran itu sangat merepotkan?",
    "Pacaran? apakah itu penting? Saya Rasa Itu Hanya Menghabiskan Waktu",
    "Motivasi tanpa aksi hanyalah halusinasi Belaka",
    "Rombongan mu bukan sama sekali ancaman bagi ku!",
    "Bicara tentang cinta? hahaha saya sudah tdk tertarik dengan itu.",
    "Kau tidak mengerti akan penderitaan ku",
]


@bot.on(poci_cmd(outgoing=True, pattern=r"qt$"))
async def _(sange):
    """Quote Gajelas"""
    await sange.edit(choice(KATAPOCONG))


CMD_HELP.update(
    {
        "quotes": f"**Plugin : **`quotes`\
        \n\n  •  **Syntax :** `{cmd}qt`\
        \n  •  **Function : **Untuk Mengirim Kata-kata quote.\
    "
    }
)

from userbot import CMD_HELP, BLACKLIST_CHAT, CMD_HANDLER as cmd
from userbot.events import register
from userbot.utils import ram_cmd

from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="pay(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**PAYMENT ACENG • STOREE \n\n DANA = 0895611203477 \n\nㅤPAYMENT ACENG • STOREE \n\nㅤGOPAY = 081270603368 \n\nㅤ★@ACENG_STOREE★ **",
        reply_to=event.reply_to_msg_id,
    )
    await event.delete()


@poci_cmd(pattern="P(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Hy kaa 🥺**")
    sleep(2)
    await xx.edit("**Assalamualaikum...**")


@poci_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam**", reply_to=event.reply_to_msg_id
    )
    await event.delete()


@poci_cmd(pattern="L(?: |$)(.*)")
async def _(event):
    xx = await edit_or_reply(event, f"**Astaghfirullah, Jawab salam dong**")
    sleep(2)
    await xx.edit("**Wa'alaikumsalam**")





CMD_HELP.update(
    {
        "salam": f"**Plugin : **`salam`\
        \n\nㅤㅤ•**Syntax** : {cmd}pay\
        \n•**Function : **Payments..\
        \n\nㅤㅤ•**Syntax** : {cmd}P\
        \n•**Function : **salam Kenal dan salam\
        \n\nㅤㅤ•**Syntax** : {cmd}l\
        \n•**Function : **Untuk Menjawab salam\
        \n\nㅤㅤ•**Syntax** :{cmd}L\
        \n•**Function : **Untuk menjawab salam\
    "
    })


CMD_HELP.update({
    "war":
    f"V\
\nUsage: Hujat Orang caper.\
\n\nJ\
\nUsage: Hujat Jamet.\
\n\nA\
\nUsage: Hujat yang gapunya muka.\
\n\nX\
\nUsage: Ngatain Grup wkwk.\
\n\nZ\
\nUsage: teruntuk petarung.\
\n\nH\
\nUsage: Coba dewek ah.\
\n\n`{cmd}atg`\
\nUsage: Istighfar 1.\
\n\n`{cmd}ast`\
\nUsage: Istighfar 2.\
\n\nO\
\nUsage: Ngatain org norak.\
\n\nG\
\nUsage: Liat Sendiri.\
\n\nK\
\nUsage: Untuk mengontoli mereka.\
\n\nN\
\nUsage: Kalo kesel coba aja.\
\n\nB\
\nUsage: Buat Ngatain Yang Suka Bacot.\
\n\nM\
\nUsage: Tersedak meledek.\
\n\nY\
\nUsage: Buat yang males adu bacot.\
\n\nC\
\nUsage: Buat menghujat.\
\n\nS\
\nUsage: Haha sokap.\
\n\nK\
\nUsage: Untuk mengontoli mereka."
})

from time import sleep

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, poci_cmd


@poci_cmd(pattern="pay(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id,
        "**PAYMENT ACENG STOREE DANA = 0895611203477 GOPAY = 081270603368**",
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

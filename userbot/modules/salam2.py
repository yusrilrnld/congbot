# Gausah kesini ngentot!!
# NGEDIT CMD YG BENER KONTOL!!!
# YANG HAPUS KREDIT GUA TANDAIN REPO LO

from userbot import CMD_HELP, BLACKLIST_CHAT, OWNDEV, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, ram_cmd

# ================= WELCOME ==================
#       HAYO YANG HAPUS KREDIT GUA JITAK
#                FROM RAM-UBOT
# ============================================

@ram_cmd(pattern="p(?: |$)(.*)")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(event, "JANGAN PAKE DISINI SALAM LO HARAM HEHEHE")
    await event.client.send_message(
        event.chat_id, "**𝐀ssalamu'alaikum gc haram**", reply_to=event.reply_to_msg_id)
    await event.delete()


@ram_cmd(pattern="gjm(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "GAK, JANGAN MAKSA YAH KONTOL!!", reply_to=event.reply_to_msg_id)
    await event.delete()


@ram_cmd(pattern="l(?: |$)(.*)")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(event, "JANGAN DISINI DI NGENTOD SALAM LO HARAM!!")
    await event.client.send_message(
        event.chat_id, "**Wa'alaikumsalam kaum dajal...**", reply_to=event.reply_to_msg_id)
    await event.delete()

@ram_cmd(pattern="gjn(?: |$)(.*)")
async def typewriter(event):
    await event.client.send_message(
        event.chat_id, "TYPING APASI YANG JELAS NGENTOD, MAKANYA KALO JARI PADA KEBAS ATAU EMANG UDAH MATI RASA, JANGAN DI PAKSAIN NGETIK TOLOL, NANTI LO LUMPUH KAYA MAMAK LO YG HARI HARINYA BARING TERUS KALO KEKAMAR MANDI HARUS DI GOTONG MIRIP PISANG TANDAN, MANA BAPAKLO PENGANGGURAN KERJAAN NYA CUMA SERABUTAN TOLOL, MIKIR NAPA SI ANJING!!!", reply_to=event.reply_to_msg_id)
    await event.delete()

@ram_cmd(pattern="yb(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**YA ANDA BENAR, BENAR BENAR HARAM UNTUK DI AJAK BERTEMAN KONTOL, MANUSIA HINA KAYA LO GA ADA KEREN KEREN NYA DI MATA GUA NGENTOD, MINIMAL LO MANDI BIAR KELIATAN FRESH GT, MUKA LAYU BANGET KAYA POHON GA PERNAH DI SIRAM TOLOL, MATA LO ITEM BEGITU MIRIP GEMBEL PASAR SENEN NGENTOD, JANGAN BELAGA LAGA MAO BERTEMEN SAMA GUA, PENGEMIS YG TAHTANYA RENDAHAN AJA OGAH ANJING BERTEMEN SAMA LO DASAR YATIM LO ANAK HARAM BAYI LONTE MUKA CABUL HATI IBLIS CUWIHHHH**", reply_to=event.reply_to_msg_id)
    await event.delete()


@ram_cmd(pattern="m(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
         event.chat_id, "**MEMEK NYA ANAK INIIIII....**")
    await event.delete()

@ram_cmd(pattern="k(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**APALO KONTOL? MAO MARAH LO, MARAH AJA LAH NGENTOD GA TAKUT TAKUT AMAT GUA KALO LO MARAH, BADAN LO KECIL KURUS KEREMPENG UDAH PERSIS BATANG POHON SINGKONG, GUA SLEDING JUGA KEJENGKANG LO 🐷**", reply_to=event.reply_to_msg_id)
    await event.delete()

@ram_cmd(pattern="gjb(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat.id, "**GAJELAS BABI, MUKA HINA LO TUH URUSIN DULU ANJING, JERAWAT NUMPUK DIMANA MANA UDH PERSIS KAYA ORANG PENYAKITAN, MANA BADAN LO BAU BANGET ANJING, APEK KAYA KASUR BASAH GA DI JEMUR, NAH ITU KASUR LO TU UDAH TAU TINGGAL DI RUMAH GUBUK KAYU TOLOL, SERING BOCOR KALO UJAN, JADI LO TIDUR SAMBIL MANDI UJAN, TAPI YANG GUA HERAN BADAN LO BAU BANGET BANGSAT, MAKAN SAMPAH LO YA?**", reply_to=event.reply_to_msg_id)
    await event.delete()

@ram_cmd(pattern="gjk(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**GAJELAS KONTOL, MAKANYA KALO MAO LAWAN TYPINGAN GUA MINIMAL LO PANDAI BERBAHASA INDONESIA DENGAN BAIK ANJING, KELAMAAN TINGGAL DI KAMPUNG SI NGENTOT, JADI GA PAHAM ARTIKULASI BAHASA GUA KAN LO, UDAH LAH MENDING DIEM AJA DI EMBER BARENG KURA KURA**", reply_to=event.reply_to_msg_id)
    await event.delete()

@ram_cmd(pattern="gbgn(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**GA BANGET LO BEGITU NGENTOT, GAYA LO AJA DI GEDE GEDEIN PADAHAL MAN ASLINYA MISKIN SE MISKIN MISKIN NYA KRANG MISKIN LO, IYALAH JELAS, LAHIR DARI ORANG TUA YG GA MAMPU MANA BAPAK LO NOH ANJING BAPAKLOO DI SIKSA SAMA MALAIKAT DALEM KUBUR TOD, MINIMAL LO DOAIN BAPAK LO JANGAN KERJAAN NYA BEGAYA DOANG MANA GA SESUAI SAMA LATAR BELAKANG KEHIDUPAN, GUA KALO JADI EMAK LO, UDH MALU BAT NAJIS DEH**", reply_to=event.reply_to_msg_id)
    await event.delete()

@ram_cmd(pattern="gls(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**GAK, LO SANGEAN TOT, DAH TAU TITIT KECIL BULUK BGTU BLAGU BLAGU NGAJAK CEWE VCS LO NGENTOT ANJING, MIKIR DULU BANGSAT JIJI BGT LAH YANG ADA SEKELAS LONTE YG DI BAYAR AJA MIKIR GOBLOK BUAT DI SEWA SAMA LO, KARNA TITIT LO TU ADA KELAINAN ANJING, PUNYA PENYAKIT KELAMIN KAN LO, DASAR SPILIS SPILIS!!!**", reply_to=event.reply_to_msg_id)
    await event.delete()


@ram_cmd(pattern="bsl(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**BAU SAWI LO ANJING, PAKE MINYAK WANGI NAPA SI KALO GA MAMPU YA MINIMAL PAKE MINYAK TELON ANJING, APA GAMAMPU JUGA? PAKE AJA MINYAK GORENG TU LO OLESIN KE SEKUJUR BADAN LO NAH ABIS TU LO NYEMPLUNG KE PENGGORENGAN EMAK LO PAS LAGI GORENG IKAN, COCOK TU YA KAN MATI AJA BEGO LO, EMAK LO JUGA SEBENERNYA TERPAKSA ANJING NGEBESARIN LO, ORG EMAK LO MANTAN LONTE, JADI ITU KARNA KECEPLOSAN AJA EH JADI LAH LO ANAK HARAM CK CK DEKK DEKK!!**", reply_to=event.reply_to_msg_id)
    await event.delete()


@ram_cmd(pattern="hoi(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**HAI, ANAK YATIM BAU KENCUR YANG SABAN HARI NGAREPIN DI SANTUNIN SAMA TETANGGA YAHAHAHA, KASIAN BANGET BOCAH NYA KALO GA ADA SANTUNAN GA MAKAN LO YA? IYALAH JELAS ANJING PAS BAPAK LO MENINGGAL TU EMAK LO LUMPUH, MAU NANGIS AJA EMAK LO TU GABISA ANJING, ORG UDH LUMPUH TOTAL YAHAHA, KASIAN BAT BOCAH NYA CIH DEH!!**", reply_to=event.reply_to_msg_id)
    await event.delete()


@ram_cmd(pattern="em(?: |$)(.*)")
async def _(event):
    await event.client.send_message(
        event.chat_id, "**EH MEMEK, PP LO PINTEREST TOLOL, GA KAYA GUA YG BENERAN GANTENG, PP PINTEREST LO DI ADU SAMA GUA JUGA MASIH GANTENGAN GUA ANJINK BANGET DAH, GUA TAU LO KENAPA PAKE PP PINTEREST, NAH KARNA WAKTU LO KECIL YAKAN, EMAK LO LAGI GORENG TEMPE BUAT MASAKIN BAPAK LO YG PENYAKITAN, NAH LO REWEL MINTA JAJAN, PAS BANGET EMAK LO GA ADA DUIT YA ORG MISKIN HEHE, LO MAKSA KAN TU MINTA DUIT, NAH EMAK LO GEDEG TU, MUKA LO DI SIRAM MINYAK GORENG PANAS, NAH SEKARANG MALAH MUKA LO CACAT KAN, MIRIP ALIEN YAHAAH, KENAPA GA DI SIRAM AIR KERAS AJA SI ANJING, BIAR MATI SKALIAN WKKWKK!!!**", reply_to=event.reply_to_msg_id)
    await event.delete()


@ram_cmd(pattern="eh(?: |$)(.*)")
async def _(typew):
    await typew.client.send_message(
        typew.chat_id, "**EH NGENTOT, INGET YE, KALO DI BILANGIN ORANG ITU DENGERIN DEK, JANGAN SOK PAHAM ANJINKK, OTAK LO ITU KAPASITAS NYA RENDAH IBARATNYA NI HP GUA RAM 8GB NAH LO CUMA 2GB YAHAHA, APAAN ANJING, MAKANYA DEK KALO KAPASITAS OTAK MASI RENDAH, PENGETAHUAN MASIH SEDIKIT, NURUT APA TOLOL KALO DI BILANGIN, KALO SOK TAU TERUS HIDUP LO GA BAKAL MAJU ANJING, EH EMANG GA BAKAL MAJU SI, HIDUP LU STUCK DI KEHIDUPAN YANG MISKIN, SAMA KAYA OTAK LO YG STUCK DALAM KEBODOHAN HEHEE!**", reply_to=typew.reply_to_msg_id)
    await typew.delete()


@ram_cmd(pattern="ucp(?: |$)(.*)")
async def _(typeq):
    if typeq.chat_id in OWNDEV:
        return await edit_or_reply(typeq, "LAH DIA DEVELOPER RAM-UBOT TOLOL")
    await typeq.client.send_message(
        typeq.chat_id, "**LU SIAPA SI NGENTOT, GAUSAH SOKAP APA SAMA GUA, NAJIS BAT JUGA GUA KENAL SAMA LO ANJING, GA PASANG PP NAMA GA JELAS BGTU, NAMA HARAM, MANUSIA HARAM, MUKA HARAM, KEHIDUPAN HARAM, LAHIR DARI ORANG TUA YANG HARAM, MAKAN LO MAKAN DUIT HARAM YA SEMUA TENTANG LO HARAM UNTUK DI KENAL DAN DI KENANG HEHEH!!!!**", reply_to=typeq.reply_to_msg_id)
    await typeq.delete()  


@ram_cmd(pattern="halo(?: |$)(.*)")
async def _(typew):
    if typew.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(typew, "GABOLEH NGATAIN MEMBER SINI NJING!!!!")
    await typew.client.send_message(
        typew.chat_id, "**HAI MEMBER ALAY, ALIANSI SAMPAH, FAMILY GAGUNA, MARGA TOLOL, SIRKEL ANJING, BOCAH AUTIS, PERKUMPULAN HARAM, PENYEMBAH KAMBING, PENCETUS KESESATAN, UTUSAN DAJAL, HARAM BGT YA KATA KATA GUA? YA IU COCOK BANGET KONTOL BUAT NGATAIN PERKUMPULAN KAYA LO PADA ANJING, YA EMANG HARAM SI PANTES BGT DI BUBARIN AJA JING!!**", reply_to=typew.reply_to_msg_id)
    await typew.delete()


@ram_cmd(pattern="loh(?: |$)(.*)")
async def _(typew):
     if typew.chat_id in BLACKLIST_CHAT:
         return await edit_or_reply(
             typew, f"**Dasar ngentot, Lo gabisa Nyoba disini anjing!!!**"
         )
     await typew.client.send_message(
        typew.chat_id, "**GC SAMPAH KAYA GINI, ISINYA CUMA GCAST SAMA FORWARD CHANNEL ANJING, PAKE SOK SOKAN NYENGGOL SANA SINI, GC MASIH DIBAWAH 10K ITU GAUSAH BELAGU DEK, DIAM AJA SIMAK, JANGAN SENGGAL SENGGOL ANJING, TAR GUA LADENIN MALAH BISA BUBAR GC LO TOD!!!**", reply_to=typew.reply_to_msg_id)
     await typew.delete()
    
CMD_HELP.update({
    "ribut":
    f"{cmd}p\
\nUsage:\
\n\n{cmd}l\
\nUsage:\
\n\n{cmd}gjm\
\nUsage:\
\n\n{cmd}gjn\
\nUsage:\
\n\n{cmd}gjb\
\nUsage:\
\n\n{cmd}yb\
\nUsage:\
\n\n{cmd}gjk\
\nUsage:"
})

CMD_HELP.update({
    "war2":
    f"{cmd}gbgn\
\nUsage:\
\n\n{cmd}bsl\
\nUsage:\
\n\n{cmd}hoi\
\nUsage:\
\n\n{cmd}eh\
\nUsage:\
\n\n{cmd}em\
\nUsage:\
\n\n{cmd}gls\
\nUsage:\
\n\n{cmd}halo\
\nUsage:\
\n\n{cmd}loh\
\nUsage:\
\n\n{cmd}ucp\
\nUsage:\
\n\n{cmd}m\
\nUsage:\
\n\n{cmd}k\
\nUsage:"
})

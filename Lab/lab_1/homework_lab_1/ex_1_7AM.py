from gmail import GMail, Message
from random import choice

gmail = GMail('dknguyen@knox.edu','Anhnangcuaanh789)')

html_content = """
<p style="text-align: center;">Cộng ho&agrave; x&atilde; hội chủ nghĩa Việt Nam</p>
<p style="text-align: center;">Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">K&iacute;nh gửi trung t&acirc;m Techkids,</p>
<p style="text-align: left;">En t&ecirc;n Nguyễn Kim Diệu. H&ocirc;m nay, thứ S&aacute;u ng&agrave;y 13, năm 2018, em xin nghỉ do {{sickness}}.</p>
<p style="text-align: left;">Em xin ch&acirc;n th&agrave;nh cảm ơn sự th&ocirc;ng cảm của thầy Huỳnh Tuấn Anh.</p>
<p style="text-align: left;">&nbsp;</p>
<p style="text-align: left;">Tr&acirc;n trọng,</p>
<p style="text-align: left;">Nguyễn Kim Diệu</p>
<p>&nbsp;</p>
"""
lydo = ["ốm", "đau bụng", "không thích học", "hạ huyết áp", "lượng đường trong máu giảm", "xe hỏng", "tắc đường", "học phí cao", "con cún nhà e không muốn e đi học"]

html_to_send = html_content.replace("{{sickness}}", choice(lydo))


msg = Message('Đơn xin nghỉ học',to='20130075@student.hust.edu.vn',html=html_to_send)

import datetime
now = datetime.datetime.now()
loop = True
while loop:
    if now.hour == 7:
        gmail.send(msg)
        loop = False
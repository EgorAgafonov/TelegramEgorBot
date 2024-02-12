import requests
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup
import easyocr
import sys
import segno
import io
from PIL import Image

# 1 -
# - ?????? ???????? ??????????? HTML-???????? (??????? ??????????? ? ???????? ????? ???????) ? ??????? ????????? lxml:

# html = requests.get("https://www.python.org/").content
# tree = lxml.html.document_fromstring(html)
# title = tree.xpath("//*[@id='dive-into-python']/ul[2]/li[1]/div[2]/p/text()")
# print(title)
#
# # ???????? ?????? ElementTree. ?? ???????????? ???????? parse()
# tree = etree.parse('Welcome to Python.org.html', lxml.html.HTMLParser())  # ?????????? ???????? ??? ???? ? ???????
# # HTML-???????. ??? HTML ? ??? ??, ??? ?? ??????? ? ????????? ? ????? ?? ????????.
#
# ul = tree.findall('/body/div/div[3]/div/section/div[2]/div[1]/div/ul/li')  # ???????? ? ???????? ?????? findall
# # ????????????? xpath. ????? ?? ??????? ??? ???????? ?????? ????????.
#
# for li in ul:
#     a = li.find('a')    # ? ?????? ???????? ???????, ??? ???????? ????????? ???????. ? ??? ??? ??? <a>. ?.?.
#                         # ???????????, ?? ??????? ????? ??????, ????? ??????? ?? ???????? ? ????????. ??????????? ?
#                         # HTML ? ??? ?????? ??? <a>.
#     print(a.text)  # ?? ????? ???? ???????? ????? ? ??? ? ????? ????? ?????????


# 2 -
# - ?????? ???????? ??????????? HTML-???????? (??????? ??????????? ? ???????? ????? ???????) ? ??????? ??????????
# bs4 import BeautifulSoup:

# base = 'https://ru.stackoverflow.com'
# html = requests.get(base).content
# soup = BeautifulSoup(html, 'lxml')
# div_container = soup.find('div', id='question-mini-list')
# a_tag = div_container.findAll('a', class_='s-link')
# file = 'lxml_lessons.txt'
# with open(file, 'w', encoding='windows-1251') as f:
#     for link in a_tag:
#         result = f"\n{link.getText()}\n" + f"\n{base + link.get('href')}\n"
#         f.write(result)
#         print(f"{link.getText()}\n" + f"{base + link.get('href')}\n")

# def text_recognition(file_path):
#     reader = easyocr.Reader(['ru', "en"])
#     result = reader.readtext(file_path, detail=0, paragraph=True)
#     return result
#
#
# def main():
#     file_object = os.path.split("\\chat_images\\test.png")
#     recognized_text = text_recognition(file_path=file_object)
#     print(recognized_text)
#
#     # 1 - ??????? ??????????? ?????? ??????????? OCR
#     recognized_string = '\n'.join(recognized_text)
#     print(recognized_string)
#
#     # 2 - ??????? ??????????? ?????? ??????????? OCR
#     for key in recognized_text:
#         print(key)


# if __name__ == "__main__":
#     main()


# qrcode_1 = segno.make_qr("https://github.com/EgorAgafonov/TelegramCurrencyBot.git")
# img = qrcode_1.to_pil(scale=25).rotate(45, expand=True)
# img.save("qrcode_scale_30.png", light="lightgreen")


out = io.BytesIO()
# Nothing special here, let Segno generate the QR code and save it as PNG in a buffer
segno.make_qr("https://github.com/EgorAgafonov/TelegramCurrencyBot.git", error='h').save(out, scale=25, kind='png')
out.seek(0)  # Important to let Pillow load the PNG
img = Image.open(out)
img = img.convert('RGB')  # Ensure colors for the output
img_width, img_height = img.size
logo_max_size = img_height // 3  # May use a fixed value as well
logo_img = Image.open('git_hub_logo.png')  # The logo
# Resize the logo to logo_max_size
logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.LANCZOS)
# Calculate the center of the QR code
box = ((img_width - logo_img.size[0]) // 2, (img_height - logo_img.size[1]) // 2)
img.paste(logo_img, box)
img.save('qrcode_with_logo.png')
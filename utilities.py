import json
import requests
import easyocr
from settings import *
import segno
import io
from PIL import Image


class ConvertionException(Exception):
    pass


class CryptoConverter:

    @staticmethod
    def convert(token: str, quantity: str, base_code: str, target_code: str, ) -> object:
        """Метод отправки GET-запроса для предоставления сведений о стоимости(amount) одной/нескольких единиц базовой
        валюты(base_code) по отношению к целевой валюте(target_code), т.е. стоимость покупки одной валюты в
        единицах другой."""

        base_url = "https://v6.exchangerate-api.com/v6/"
        response = requests.get(base_url + token + "pair/" + f"{base_code}/" + f"{target_code}/" + str(quantity))

        status = response.status_code
        result = ""
        try:
            result = response.json()
        except json.JSONDecodeError:
            result = response.text

        try:
            check_1 = float(quantity)
            check_2 = quantity.isdigit()
        except ValueError:
            raise ConvertionException(f"Ошибка!\n"
                                      f"Указанное значение: '{quantity}' не является числом.")

        if base_code == target_code:
            raise ConvertionException(f"Ошибка!\nУказаны две одинаковые валюты или числовое значение вместо "
                                      f"буквенного.\n"
                                      f"Логика вышла из чата😜.\n "
                                      f"Вот корректный пример ввода: '100 USD RUB'")
        try:
            check_1 = keys[base_code]
            check_2 = base_code.isalpha()
        except KeyError:
            raise ConvertionException(f"Ошибка!\n"
                                      f"Указан неверный код валюты или числовое значение вместо буквенного: "
                                      f"{base_code}.\n")
        try:
            check_1 = keys[target_code]
            check_2 = target_code.isalpha()
        except KeyError:
            raise ConvertionException(f"Ошибка!\n"
                                      f"Указан неверный код валюты или числовое значение вместо буквенного: "
                                      f"'{target_code}'.\n")

        return status, result


class TextImageReader:

    @staticmethod
    def text_recognition(file_path: str, langs: list) -> str:
        """Метод для оптического распознавания текста(OCR) на изображении, переданного пользователем в чат бота.
        Возвращает распознанный текст в виде строкового, машинописного кода. В атрибут file_path передается строковое
        значение пути к файлу для распознавания. """

        reader = easyocr.Reader(langs)
        recognized_List = reader.readtext(file_path, detail=0, paragraph=True, text_threshold=0.5)
        recognized_string = '\n'.join(recognized_List)
        result = recognized_string.replace("<", "'").replace(">", "'").replace("/", "'")
        return result


class QRcodeMaker:
    @staticmethod
    def make_QR_code(content):
        qrcode = segno.make_qr(content, error='h')
        qrcode.save("qrcode_scale_25.png", scale=25, light='lightgreen')
        result = open("qrcode_scale_25.png", mode="rb")
        return result


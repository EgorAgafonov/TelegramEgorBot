Telegram-бот для конвертации валют, распознавания текстов,
генерации QR-кодов и предоставления данных о юридических лицах РФ (ЕГРЮЛ).


Чат-бот, написанный в учебных целях для ознакомления с библиотекой telebot мессенджера Telegram.
Для обработки запросов об обменных курсах валют и предоставления сведений о юридических лицах РФ (ЕГРЮЛ), используются 
API-сервисы https://dadata.ru/api и https://www.exchangerate-api.com/ (необходима регистрация и получение TOKEN-ключей).
Запросы оптического распознавания текста (OCR) и генерации QR-кодов реализованы с помощью библиотек EasyOCR Reader и Segno.

Структура проекта представлена:
1) модулем main.py - точка входа с основной программой бота; 
2) модулем utilities.py с классами методов для реализации основных функций бота;
3) модулем settings, содержащим переменные с параметрами данных для работы бота;
4) директорией chat_images для обработки и временного хранения изображений из бота;

Классы, методы и функции проекта содержат строки документации.

Агафонов Е.А., 2024 г.

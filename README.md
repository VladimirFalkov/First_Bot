# Проект catBOT

CatBot это телеграм бот, присылающий фото котиков пользователю чем поднимает ему настроение.

## Установка

1. Клонируйте репозиторий
2. Создайте репозиторий
3. Установите зависимости `pip install -r requirements.txt`
4. Создайте файл `settings.py`
5. Впишите в settings.py переменные:
```
API_KEY = 'API-ключ бота'
PROXY_URL = 'Адрес ПРОКСИ'
PROXY_USERNAME = 'логин на ПРОКСИ'
PROXY_PASSWORD = 'пароль на ПРОКСИ'
USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
```
6. Запустите Бота командой 'python mybot.py'
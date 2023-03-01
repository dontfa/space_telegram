# Загрузка картинок на космическую тематику из различных источников
Скрипт выполняет загрузку картинок из свободных источников на сайтах: https://api.spacexdata.com и https://api.nasa.gov


### Как установить
Python3 уже должен быть установлен. Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей.
```commandline
pip install -r requirements.txt
```
Рекомендуется использовать виртуальное окружение для изоляции пректа.

### Использование переменных окружения
Для использования стороннего API необходим токен доступа предоставляемый сервисом https://bitly.com после регистрации на ресурсе. Полученный токен должен быть размещен в переменной окружения BITLY_TOKEN.

### Цель проекта
Проект создан в образовательных целях в рамках обучения на онлайн-курсе dvmn.org.
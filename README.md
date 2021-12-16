# OhMyCertAPI

API для получения именных сертификатов, разработанный в учебных целях.
Проект для [Русской школы программирования](https://codeschool.it-edu.com)

## Что под капотом?

4 библиотеки: [PyPDF2](https://pypi.org/project/PyPDF2/), [reportlab](https://pypi.org/project/reportlab/) - для работы с pdf, [Flask](https://flask.palletsprojects.com/en/2.0.x/) и [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/) - для API

Посмотрим на файлы
-------------------

      app.py              для запуска api
      pdf2cert.py         для создания сертификата
      requirements.txt    необходимые библиотеки
      config.py           конфигурация (создаете по примеру config.example.py)
      DejaVuSerif.ttf     файл шрифта поддерживающий кириллицу
      templates/          папка с шаблонами для сертификатов
      files/              папка с сертификатами


## Установка

- Создаете конфигурационный файл config.py
- Не забываем установить зависимости `pip install -r requirements.txt`
- Добавляете в папку templates шаблоны pdf и/или шаблон по умолчанию (см. название файла в настройках, можете переименовать)


**PS:**
API работает с учебным шаблоном pdf, который в репозиторий не загружен.
Для своего шаблона поэкспериментируйте с pdf2cert.py

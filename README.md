# api_final
Проект «API для Yatube»

Как запустить проект:

1. Cоздать и активировать виртуальное окружение:

    python3 -m venv env
    source env/bin/activate

2. Установить зависимости из файла requirements.txt:

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

3. Выполнить миграции:

    python3 manage.py migrate

4. Запустить проект:

   python3 manage.py runserver


WebU3Lab

WebU3Lab

WebU3Lab — это простое веб-приложение для управления задачами, разработанное с использованием Flask. Оно позволяет добавлять, просматривать и удалять задачи.
Начало работы
Требования

    Python 3.8 или выше

    pip

    Docker и Docker Compose (опционально)

Установка

    Клонируйте репозиторий:

    git clone https://github.com/Unweared/webu3lab.git
    cd webu3lab

    Установите зависимости:

    pip install -r requirements.txt

    Запустите приложение:

    python app.py

Приложение будет доступно по адресу: http://localhost:5000
Использование Docker

    Постройте и запустите контейнеры:

    docker-compose up --build

Приложение будет доступно по адресу: http://localhost:5000
Тестирование

Для запуска тестов используйте:

pytest


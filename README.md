# Веб-приложение на Flask с MariaDB, Nginx и GitLab (через HTTPS)

## Запуск проекта

1. Установите Docker и Docker Compose
2. Поместите SSL-сертификаты в папку `certs/`:
   - `fullchain.pem`
   - `privkey.pem`
3. Запустите приложение:
```bash
docker-compose up --build

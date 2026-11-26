# Тестовый сервис

Небольшой проект для проверки работы нескольких экземпляров FastAPI за Nginx в Docker Compose.

## Состав

- `backend-1`, `backend-2`, `backend-3` — экземпляры FastAPI с разными значениями `INSTANCE_ID`.
- `nginx` — принимает запросы на порту `80` и проксирует `/api/` к upstream-группе из трёх бэкендов.
- `GET /api/health` возвращает идентификатор ответившего экземпляра, например `{"health":"Backend_1"}`.

## Запуск

Из каталога проекта:

```bash
docker compose up --build -d
```

Отправить запрос из WSL или Linux:

```bash
curl http://127.0.0.1/api/health
```

В PowerShell используйте `curl.exe`:

```powershell
curl.exe http://127.0.0.1/api/health
```

## Проведённое тестирование
```bash
for i in {1..6}; do curl -s http://127.0.0.1/api/health; echo ""; done
```
После запуска команды получили ожидаемый вывод балансировки запросов при помощи Round Robin
{"health":"Backend_2"}
{"health":"Backend_3"}
{"health":"Backend_1"}
{"health":"Backend_2"}
{"health":"Backend_3"}
{"health":"Backend_1"}
{"health":"Backend_2"}
{"health":"Backend_3"}


После запуска команды получили ожидаемый вывод балансировки запросов при помощи Weighted Round Robin

{"health":"Backend_3"}
{"health":"Backend_2"}
{"health":"Backend_1"}
{"health":"Backend_2"}
{"health":"Backend_1"}
{"health":"Backend_2"}
{"health":"Backend_2"}
{"health":"Backend_1"}
{"health":"Backend_2"}
{"health":"Backend_3"}
{"health":"Backend_2"}
{"health":"Backend_1"}

```bash
for i in {1..100}; do curl -s http://127.0.0.1/api/health; echo ""; done | sort | uniq -c
```

37 {"health":"Backend_1"}
50 {"health":"Backend_2"}
13 {"health":"Backend_3"}
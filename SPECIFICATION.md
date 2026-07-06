# Спецификация проекта "Менеджер задач"

## Сущности
- **User**: id (int), username (str), email (str)
- **Task**: id (int), title (str), description (str), status (enum: new, in_progress, done), user_id (FK), created_at, updated_at
- **Tag**: id (int), name (str)
- **Связь**: Task <-> Tag (многие ко многим)

## Требуемые эндпоинты (REST API)
- POST /users/ — регистрация
- POST /tasks/ — создать задачу (требуется аутентификация, но пока пропускаем)
- GET /tasks/ — список всех задач (с фильтрацией по статусу и тегу)
- GET /tasks/{id} — получить задачу
- PUT /tasks/{id} — обновить задачу
- DELETE /tasks/{id} — удалить задачу
- POST /tasks/{id}/tags/ — добавить тег к задаче

## Технические требования
- Python 3.10+
- FastAPI
- PostgreSQL
- SQLAlchemy (или сырой SQL — решим на сессии)
- Docker + docker-compose
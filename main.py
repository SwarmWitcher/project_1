import requests

# Создаем список задач. Каждая задача - это словарь с ключами id, title, status.
tasks = [
    {"id": 1, "title": "Купить продукты", "status": "new"},
    {"id": 2, "title": "Помыть посуду", "status": "in_progress"},
    {"id": 3, "title": "Сделать уроки", "status": "done"},
    {"id": 4, "title": "Позвонить маме", "status": "new"}
]

# Функция фильтрации задач по статусу
def filter_by_status(status):
    """Принимает строку со статусом и возвращает список задач с этим статусом"""
    result = [] # пустой список реультатов
    for task in tasks: # перебираем все задачи
        if task["status"] == status: # если статус задачи совпадает с переданным
            result.append(task) # добавляем задачу в список результатов
    return result # возвращаем список подходящих задач

# Выводим все задачи в красивом формате "ID: ... | Title: ... | Status: ..."
print("\nВсе задачи:")
for task in tasks:
    print(f"ID: {task['id']} | Title: {task['title']} | Status: {task['status']}")

# Функция для GET-запроса к GitHub API
def get_github_status():
    url = "https://api.github.com"
    response = requests.get(url)
    print(f"Статус-код ответа от GitHub: {response.status_code}")
    return response.status_code

get_github_status()

# Проверяем работу фильтрации по статусу
print("\nЗадачи со статусом 'new':")
new_tasks = filter_by_status("new")
for task in new_tasks:
    print(f"ID: {task['id']} | Title: {task['title']} | Status: {task['status']}")

print("\nЗадачи со статусом 'done':")
done_tasks = filter_by_status("done")
for task in done_tasks:
    print(f"ID: {task['id']} | Title: {task['title']} | Status: {task['status']}")
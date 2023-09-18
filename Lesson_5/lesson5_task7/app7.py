# Создать RESTful API для управления списком задач.
# Приложение должно использовать FastAPI и поддерживать следующие функции:
# - Получение списка всех задач;
# - Получение информации о задаче по её ID;
# - Добавление новой задачи;
# - Обновление информации о задаче по её ID;
# - Удаление задачи по её ID.
# Каждая задача должна содержать следующие поля:
# ID (целое число), Название (строка), Описание (строка), Статус (строка): "todo", "in progress", "done".
#
#  =(продолжение)=
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте функцию get_tasks для получения списка всех задач (метод GET).
# Создайте функцию get_task для получения информации о задаче по её ID (метод GET).
# Создайте функцию create_task для добавления новой задачи (метод POST).
# Создайте функцию update_task для обновления информации о задаче по её ID (метод PUT).
# Создайте функцию delete_task для удаления задачи по её ID (метод DELETE).

import logging
from fastapi import FastAPI
from lesson5_task7.models7 import TaskBase, db7, Task, Base, engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
Base.metadata.create_all(bind=engine)
app7 = FastAPI()


@app7.get("/tasks/")
async def read_root():
    res = []
    logger.info('Отработал GET запрос.')
    tasks = db7.query(TaskBase).all()
    for task in tasks:
        res.append(
            f"  task_id: {task.task_id}, title: {task.title}, description: {task.description}, status: {task.status}  ")
    return res


@app7.get("/tasks/{task_id}")
async def read_root(task_id: int):
    logger.info('Отработал GET запрос.')
    task = db7.query(TaskBase).filter(TaskBase.task_id == task_id).first()
    return f"Task:  task_id: {task.task_id}, title: {task.title}, description: {task.description}, status: {task.status}"


@app7.post("/tasks/{task_id}")
async def create_item(task_id: int, task: Task):
    logger.info('Отработал POST запрос.')
    tasks = db7.query(TaskBase).filter(TaskBase.task_id == task_id).all()
    for task in tasks:
        if task.task_id == task_id:
            return f'Task already exist!'
    else:
        new_item = TaskBase(task_id=task.task_id, title=task.title, description=task.description, status=task.status,
                            is_del=False)
        db7.add(new_item)
        db7.commit()
        # tasks.append(item)
        return f'Task: {task}'


@app7.put("/tasks/{task_id}")
async def update_item(task_id: int, task_upd: Task):
    logger.info(f'Отработал PUT запрос для task id = {task_id}.')
    task = db7.query(TaskBase).filter(TaskBase.task_id == task_id).first()
    task.title = task_upd.title
    task.description = task_upd.description
    task.status = task_upd.status
    db7.commit()
    return {"task_id": task_id, "task": task_upd}


@app7.delete("/tasks/{task_id}")
async def delete_item(task_id: int):
    logger.info(f'Отработал DELETE запрос для task id = {task_id}.')
    tasks = db7.query(TaskBase).filter(TaskBase.task_id == task_id).all()
    for task in tasks:
        db7.delete(task)
        db7.commit()
    return {"task_id": task_id}

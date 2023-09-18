# Необходимо создать API для управления списком задач.
# Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# - GET /tasks - возвращает список всех задач;
# - GET /tasks/{id} - возвращает задачу с указанным идентификатором;
# - POST /tasks - добавляет новую задачу;
# - PUT /tasks/{id} - обновляет задачу с указанным идентификатором;
# - DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса и ответа.
# Для этого использовать библиотеку Pydantic.

import logging
from fastapi import FastAPI
from lesson5_task8.models8 import TaskBase, db8, Task, Base, engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
Base.metadata.create_all(bind=engine)
app8 = FastAPI()


@app8.get("/tasks/")
async def read_root():
    res = []
    logger.info('Отработал GET запрос.')
    tasks = db8.query(TaskBase).all()
    for task in tasks:
        res.append(
            f"task_id: {task.task_id}, title: {task.title}, description: {task.description}, status: {task.status}  ")
    return res


@app8.get("/tasks/{task_id}")
async def read_root(task_id: int):
    logger.info('Отработал GET запрос.')
    task = db8.query(TaskBase).filter(TaskBase.task_id == task_id).first()
    return f"Task:  task_id: {task.task_id}, title: {task.title}, description: {task.description}, status: {task.status}"


@app8.post("/tasks/")
async def create_task(new_task: Task):
    task_id = 1
    logger.info('Отработал POST запрос.')
    tasks = db8.query(TaskBase).all()
    if db8.query(TaskBase.task_id).first():
        for task in tasks:
            if task_id == task.task_id:
                task_id += 1
            else:
                break
        new_item = TaskBase(task_id=task_id, title=new_task.title, description=new_task.description,
                            status=new_task.status, is_del=False)
        db8.add(new_item)
        db8.commit()
        return f'Task: {new_item}'

    else:
        new_item = TaskBase(task_id=task_id, title=new_task.title, description=new_task.description,
                            status=new_task.status, is_del=False)
        db8.add(new_item)
        db8.commit()
        return f'Task: {new_item}'


@app8.post("/tasks/{task_id}")
async def create_item(task_id: int, task: Task):
    logger.info('Отработал POST запрос.')
    tasks = db8.query(TaskBase).filter(TaskBase.task_id == task_id).all()
    for task in tasks:
        if task.task_id == task_id:
            return f'Task already exist!'
    else:
        new_item = TaskBase(task_id=task.task_id, title=task.title, description=task.description, status=task.status,
                            is_del=False)
        db8.add(new_item)
        db8.commit()
        return f'Task: {task}'


@app8.put("/tasks/{task_id}")
async def update_item(task_id: int, task_upd: Task):
    logger.info(f'Отработал PUT запрос для task id = {task_id}.')
    task = db8.query(TaskBase).filter(TaskBase.task_id == task_id).first()
    task.title = task_upd.title
    task.description = task_upd.description
    task.status = task_upd.status
    db8.commit()
    return {"task_id": task_id, "task": task_upd}


@app8.delete("/tasks/{task_id}")
async def delete_item(task_id: int):
    logger.info(f'Отработал DELETE запрос для task id = {task_id}.')
    tasks = db8.query(TaskBase).filter(TaskBase.task_id == task_id).all()
    for task in tasks:
        db8.delete(task)
        db8.commit()
    return {"task_id": task_id}

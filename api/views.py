from ninja import NinjaAPI
from api.models import Task
from django.shortcuts import get_object_or_404
from .schema import TaskIn,TaskOut
from typing import List

api = NinjaAPI()

@api.post("/task/")
def create_task(request, payload:TaskIn):
    task = Task.objects.create(**payload.dict())
    return {"id": task.id}

@api.get("/task/{task_id}", response=TaskOut)
def get_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task_data = {
        "id": task.id,
        "owner": task.owner,
        "title": task.title,
        "content": task.content,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
    }
    return TaskOut(**task_data)


@api.get("/tasks", response=List[TaskOut])
def list_tasks(request):
    task = Task.objects.all()
    return task


@api.put("/task/{task_id}")
def update_Task(request, task_id: int, payload:TaskIn):
    task= get_object_or_404(Task, id=task_id)
    for attr, value in payload.dict().items():
        setattr(task, attr, value)
    task.save()
    return {"success": True}


@api.delete("/task/{task_id}")
def delete_employee(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return {"success": True}
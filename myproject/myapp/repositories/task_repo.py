from myapp.models import Task

class TaskRepository:
    def get_all_tasks(self):
        return Task.objects.all()

    def get_task_by_id(self, task_id):
        return Task.objects.filter(task_id=task_id).first()

    def add_task(self, task_data):
        task = Task(**task_data)
        task.save()
        return task

    def update_task(self, task_id, task_data):
        task = self.get_task_by_id(task_id)
        if task:
            for field, value in task_data.items():
                setattr(task, field, value)
            task.save()
        return task

    def delete_task(self, task_id):
        task = self.get_task_by_id(task_id)
        if task:
            task.delete()
        return task

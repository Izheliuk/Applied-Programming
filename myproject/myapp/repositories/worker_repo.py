from myapp.models import Worker

class WorkerRepository:
    def get_all_workers(self):
        return Worker.objects.all()

    def get_worker_by_id(self, worker_id):
        return Worker.objects.filter(worker_id=worker_id).first()

    def add_worker(self, worker_data):
        worker = Worker(**worker_data)
        worker.save()
        return worker

    def update_worker(self, worker_id, worker_data):
        worker = self.get_worker_by_id(worker_id)
        if worker:
            for field, value in worker_data.items():
                setattr(worker, field, value)
            worker.save()
        return worker

    def delete_worker(self, worker_id):
        worker = self.get_worker_by_id(worker_id)
        if worker:
            worker.delete()
        return worker

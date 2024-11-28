from myapp.models import RepairProject

class RepairProjectRepository:
    def get_all_projects(self):
        return RepairProject.objects.all()

    def get_project_by_id(self, project_id):
        return RepairProject.objects.filter(project_id=project_id).first()

    def add_project(self, project_data):
        project = RepairProject(**project_data)
        project.save()
        return project

    def update_project(self, project_id, project_data):
        project = self.get_project_by_id(project_id)
        if project:
            for field, value in project_data.items():
                setattr(project, field, value)
            project.save()
        return project

    def delete_project(self, project_id):
        project = self.get_project_by_id(project_id)
        if project:
            project.delete()
        return project

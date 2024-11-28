from myapp.models import Client

class ClientRepository:
    def get_all_clients(self):
        return Client.objects.all()

    def get_client_by_id(self, client_id):
        return Client.objects.filter(client_id=client_id).first()

    def add_client(self, client_data):
        client = Client(**client_data)
        client.save()
        return client

    def update_client(self, client_id, client_data):
        client = self.get_client_by_id(client_id)
        if client:
            for field, value in client_data.items():
                setattr(client, field, value)
            client.save()
        return client

    def delete_client(self, client_id):
        client = self.get_client_by_id(client_id)
        if client:
            client.delete()
        return client

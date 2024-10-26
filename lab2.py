class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def change_name(self, new_name):
        self.name = new_name
        return f"Name changed to: {self.name}"

    def display_info(self):
        return f"Person Info - Name: {self.name}, ID: {self.id_number}"

    def from_string(person_string):
        name, id_number = person_string.split(',')
        return Person(name.strip(), id_number.strip())
    
    def to_string():(pearson_string):
        name, id_number = person_string.split(',')
        return Person(name.strip(), id_number.strip())

class Service:
    def __init__(self, name, cost_per_unit, unit):
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.unit = unit

    def calculate_cost(self, quantity):
        return self.cost_per_unit * quantity

    def display_info(self):
        return f"Service - Name: {self.name}, Cost: {self.cost_per_unit} per {self.unit}"


class Client(Person):
    def __init__(self, name, id_number, contact_info):
        super().__init__(name, id_number)
        self.contact_info = contact_info

    def display_info(self):
        return f"Client Info - Name: {self.name}, ID: {self.id_number}, Contact: {self.contact_info}"


class Order:
    def __init__(self, client):
        self.client = client
        self.services = []

    def add_service(self, service, quantity):
        self.services.append((service, quantity))

    def calculate_total(self):
        return sum(service.calculate_cost(quantity) for service, quantity in self.services)

    def display_order_details(self):
        details = [f"Order for {self.client.name}:"]
        for service, quantity in self.services:
            details.append(f"{service.name}: {quantity} {service.unit} - Total: {service.calculate_cost(quantity)}")
        details.append(f"Total Order Cost: {self.calculate_total()}")
        return "\n".join(details)


class Company:
    def __init__(self, name):
        self.name = name
        self.services = []

    def add_service(self, service):
        self.services.append(service)

    def show_services(self):
        return "\n".join(service.display_info() for service in self.services)

    def create_order(self, client):
        return Order(client)


class Admin(Person):
    def __init__(self, name, id_number):
        super().__init__(name, id_number)

    def display_info(self):
        return f"Admin Info - Name: {self.name}, ID: {self.id_number}"


if __name__ == "__main__":
    client1 = Client("Олександр Іванов", "C001", "ivanov@example.com")
    admin = Admin("Адміністратор", "A001")
    
    company = Company("БудКомфорт")

    painting = Service("Фарбування стін", 100, "кв. метр")
    flooring = Service("Укладання підлоги", 150, "кв. метр")
    
    company.add_service(painting)
    company.add_service(flooring)

    print(company.show_services())

    order = company.create_order(client1)
    order.add_service(painting, 50) 
    order.add_service(flooring, 30)  
    print(order.display_order_details())

    print(client1.display_info())
    print(admin.display_info())

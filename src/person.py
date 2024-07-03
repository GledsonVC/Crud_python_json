import json

class Person:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }
    
    @staticmethod
    def from_dict(data):
        return Person(
            id=data['id'],
            name=data['name'],
            phone=data['phone'],
            email=data['email']
        )
    
    @staticmethod
    def load_from_json(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return [Person.from_dict(item) for item in data]

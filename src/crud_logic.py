import json
import os
from src.person import Person

class CRUDLogic:
    def __init__(self):
        self.filename = 'data/persons.json'
        if not os.path.exists(self.filename):
            self.create_empty_json()
        self.persons = Person.load_from_json(self.filename)
        self.editing_person_id = None
    
    def create_empty_json(self):
        with open(self.filename, 'w') as f:
            json.dump([], f)
    
    def get_persons(self):
        return self.persons
    
    def set_editing_person_id(self, person_id):
        self.editing_person_id = person_id
    
    def add_person(self, name, phone, email):
        if not name or not (phone or email):
            return "Nome e pelo menos um contato (telefone ou email) são obrigatórios."
        
        new_id = max([person.id for person in self.persons], default=0) + 1
        new_person = Person(id=new_id, name=name, phone=phone, email=email)
        self.persons.append(new_person)
        self.save_to_json()
        return None
    
    def update_person(self, name, phone, email):
        if not name or not (phone or email):
            return "Nome e pelo menos um contato (telefone ou email) são obrigatórios."
        
        if self.editing_person_id is None:
            return "Nenhuma pessoa selecionada para atualização."
        
        for person in self.persons:
            if person.id == self.editing_person_id:
                person.name = name
                person.phone = phone
                person.email = email
                break
        self.save_to_json()
        self.editing_person_id = None
        return None
    
    def delete_person(self, person_id):
        self.persons = [person for person in self.persons if person.id != person_id]
        self.save_to_json()
    
    def search_person(self, query):
        return [person for person in self.persons if query in person.name.lower()]
    
    def save_to_json(self):
        with open(self.filename, 'w') as f:
            json.dump([person.to_dict() for person in self.persons], f, indent=4)

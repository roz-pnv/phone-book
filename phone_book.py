#contact book classes
import re 
import os
import json

class  contact_book():
    contacts = []

    def __init__(self, name: str, phone_number: int, email_address: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email_address
        

    def add_contact(self):
        if not self.check_phone_number(self.phone_number):
            print("Invalid phone number!")
            return
        if not self.check_email_address(self.email):
            print("Invalid email address!")
            return
        self.contacts.append(dict(name=self.name, phone=self.phone_number, email=self.email))
        

    def edit_contact(self, name, phone=None, email=None):
        for i in self.contacts:
            if i['name'] == name:
                if phone and self.check_phone_number(phone):
                    i['phone'] = phone
                if email and self.check_email_address(email):
                    i['email']= email
                return 

        print("Contact not found!")


    def delete_contact(self, name):
        for l in self.contacts:
            if l['name'] == name:
                self.contacts.remove(l)
                print("Contact deleted.")
                return
            
        print("Contact not found!")


    def search_contact(self, name):
        for l in self.contacts:
            if l['name'] == name:
                for k,v in l.items():
                    print(f'{k}: {v}', end="  ")
                print("\n")
                return
            
        print("Contact not found!")


    def show_contacts(self):
        for key, value in enumerate(self.sort_contacts()):
            print(f'{key+1} ', end=" ")
            for k,v in value.items():
                print(f'{k}: {v}', end="  ")
            print("\n")


    def sort_contacts(self):
        self.contacts = sorted(self.contacts, key=lambda x: x['name'])
        return self.contacts


    def save_to_file(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'contacts.json')
        with open(file_path, 'w') as f:
            json.dump(self.sort_contacts(), f, indent=4)


    def load_from_file(self):
        try:
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, 'contacts.json')
            with open(file_path, 'r') as f:
                data = json.load(f)
                for l in data:
                    self.contacts.append(l)
        except json.JSONDecodeError:
            return 


    @staticmethod
    def check_phone_number(phone_number):
        if not re.match(r'^09[0-9]{9}$', str(phone_number)):
            return False
        return True
    

    @staticmethod
    def check_email_address(phone_number):
        if not re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$', str(phone_number)):
            return False
        return True


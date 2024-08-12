#contact book classes

import re 
import json

class contact():
    def __init__(self, name: str, phone_number: int, email_address: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email_address


    

    

class  contact_book():
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name: str, phone_number: int, email_address: str):
        if not self.check_phone_number(phone_number):
            pass
        if not self.check_email_address(email_address):
            pass

    def edit_contact(self, ):
        pass

    def delete_contact():
        pass 


    @staticmethod
    def check_phone_number(phone_number):
        if re.match(r'^09[0-9]{9}$', str(phone_number)):
            return False
        return True
    

    @staticmethod
    def check_email_address(phone_number):
        if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}$', str(phone_number)):
            return False
        return True




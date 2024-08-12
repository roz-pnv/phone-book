#main 
from phone_book import contact_book

def main():
    contacts = contact_book.load_from_file()
    while True:
        action = input("Choose an action: add, edit, delete, show, save, exit: ")
        if action == 'add':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")

            new_contact = contact_book(name, phone, email)
            new_contact.add_contact()

        elif action == 'edit':
            name = input("Name of contact to edit: ")
            phone = input("New phone (leave empty if no change): ")
            email = input("New email (leave empty if no change): ")

            new_contact.edit_contact(name, phone if phone else None, email if email else None)

        elif action == 'delete':
            name = input("Name of contact to delete: ")

            new_contact.delete_contact(name)
            
        elif action == 'show':
            contact_book.show_contacts(contacts)
        elif action == 'save':
            contact_book.save_to_file(contacts)
        elif action == 'exit':
            contact_book.save_to_file(contacts)
            break
        else:
            print("Invalid action. Please try again.")


main()

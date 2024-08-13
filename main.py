#main 
from phone_book import contact_book

def main():
    new_contact = contact_book('name', 0, 'email')
    new_contact.load_from_file()
    while True:
        action = input("Choose an action: add, edit, delete, search, show, sort, save, exit: ")
        if action == 'add':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")

            new_contact = contact_book(name, phone, email)
            new_contact.add_contact()

        elif action == 'edit':
            name = input("Name of contact to edit: ")

            new_name = input("New name (leave empty if no change): ")
            phone = input("New phone (leave empty if no change): ")
            email = input("New email (leave empty if no change): ")

            new_contact.edit_contact(name,new_name if new_name else None, phone if phone else None, email if email else None)

        elif action == 'delete':
            name = input("Name of contact to delete: ")
            new_contact.delete_contact(name)

        elif action == 'search':
            name = input("Name of contact to search: ")
            new_contact.search_contact(name)
            
        elif action == 'show':
            new_contact.show_contacts()

        elif action == 'sort':
            new_contact.sort_contacts()
            print("Your contact list sorted successfully")

        elif action == 'save':
            new_contact.save_to_file()

        elif action == 'exit':
            new_contact.save_to_file()
            break
        
        else:
            print("Invalid action. Please try again.")


main()

import psycopg2
import csv
import pandas as pd
from db_config import connect

class PhoneBook:
    def __init__(self):
        self.conn = connect()
        if self.conn is not None:
            self.cursor = self.conn.cursor()
            self.create_tables()
        else:
            print("Failed to connect to the database")
            exit(1)

    def create_tables(self):
        """Create the PhoneBook table if it doesn't exist"""
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            phone VARCHAR(20) UNIQUE NOT NULL
        );
        '''
        try:
            self.cursor.execute(create_table_query)
            self.conn.commit()
            print("PhoneBook table created successfully.")
        except (Exception, psycopg2.Error) as error:
            print(f"Error creating table: {error}")
            self.conn.rollback()

    def insert_contact(self, first_name, last_name, phone):
        """Insert a new contact into the PhoneBook"""
        insert_query = '''
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (%s, %s, %s)
        RETURNING id;
        '''
        try:
            self.cursor.execute(insert_query, (first_name, last_name, phone))
            contact_id = self.cursor.fetchone()[0]
            self.conn.commit()
            print(f"Contact added successfully with ID: {contact_id}")
            return contact_id
        except (Exception, psycopg2.Error) as error:
            print(f"Error inserting contact: {error}")
            self.conn.rollback()
            return None

    def upload_from_csv(self, csv_file_path):
        """Upload contacts from a CSV file"""
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                
                for row in reader:
                    if len(row) >= 3:
                        first_name = row[0]
                        last_name = row[1]
                        phone = row[2]
                        self.insert_contact(first_name, last_name, phone)
                
                print("Contacts imported successfully from CSV file.")
        except FileNotFoundError:
            print(f"Error: The file '{csv_file_path}' was not found.")
        except Exception as error:
            print(f"Error uploading from CSV: {error}")

    def update_contact(self, search_value, field_to_update, new_value):
        """Update a contact's first name or phone number"""
        if field_to_update not in ['first_name', 'last_name', 'phone']:
            print("Error: You can only update 'first_name', 'last_name', or 'phone'")
            return False
            
        # First, check if the contact exists
        search_query = '''
        SELECT id FROM phonebook
        WHERE first_name = %s OR last_name = %s OR phone = %s;
        '''
        
        try:
            self.cursor.execute(search_query, (search_value, search_value, search_value))
            result = self.cursor.fetchone()
            
            if result is None:
                print(f"No contact found with '{search_value}'")
                return False
                
            # Update the contact
            update_query = f'''
            UPDATE phonebook
            SET {field_to_update} = %s
            WHERE id = %s;
            '''
            
            self.cursor.execute(update_query, (new_value, result[0]))
            self.conn.commit()
            print(f"Contact updated successfully.")
            return True
            
        except (Exception, psycopg2.Error) as error:
            print(f"Error updating contact: {error}")
            self.conn.rollback()
            return False

    def search_contacts(self, search_term=None, field=None):
        """Search contacts with optional filters"""
        try:
            if search_term and field:
                if field not in ['first_name', 'last_name', 'phone']:
                    print("Invalid field. Use 'first_name', 'last_name', or 'phone'")
                    return []
                
                query = f'''
                SELECT * FROM phonebook
                WHERE {field} ILIKE %s
                ORDER BY id;
                '''
                self.cursor.execute(query, (f'%{search_term}%',))
                
            else:
                # Return all contacts if no search term is provided
                query = '''
                SELECT * FROM phonebook
                ORDER BY id;
                '''
                self.cursor.execute(query)
                
            contacts = self.cursor.fetchall()
            return contacts
            
        except (Exception, psycopg2.Error) as error:
            print(f"Error searching contacts: {error}")
            return []

    def delete_contact(self, search_value):
        """Delete a contact by username or phone"""
        try:
            # First check if the contact exists
            delete_query = '''
            DELETE FROM phonebook
            WHERE first_name = %s OR last_name = %s OR phone = %s
            RETURNING id;
            '''
            
            self.cursor.execute(delete_query, (search_value, search_value, search_value))
            deleted = self.cursor.fetchone()
            
            if deleted:
                self.conn.commit()
                print(f"Contact with ID {deleted[0]} deleted successfully.")
                return True
            else:
                print(f"No contact found with '{search_value}'")
                return False
                
        except (Exception, psycopg2.Error) as error:
            print(f"Error deleting contact: {error}")
            self.conn.rollback()
            return False

    def display_contacts(self, contacts):
        """Display contacts in a formatted table"""
        if not contacts:
            print("No contacts found.")
            return
            
        df = pd.DataFrame(contacts, columns=['ID', 'First Name', 'Last Name', 'Phone'])
        print(df.to_string(index=False))

    def close_connection(self):
        """Close the database connection"""
        if self.conn:
            if self.cursor:
                self.cursor.close()
            self.conn.close()
            print("PostgreSQL connection closed.")

def main():
    phonebook = PhoneBook()
    
    while True:
        print("\nPhoneBook Menu:")
        print("1. Add a new contact")
        print("2. Upload contacts from CSV file")
        print("3. Update a contact")
        print("4. Search contacts")
        print("5. View all contacts")
        print("6. Delete a contact")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone = input("Enter phone number: ")
            phonebook.insert_contact(first_name, last_name, phone)
            
        elif choice == '2':
            csv_file = input("Enter the path to the CSV file: ")
            phonebook.upload_from_csv(csv_file)
            
        elif choice == '3':
            search_value = input("Enter a name or phone number to find the contact: ")
            print("What would you like to update?")
            print("1. First Name")
            print("2. Last Name")
            print("3. Phone Number")
            update_choice = input("Enter your choice (1-3): ")
            
            field_map = {'1': 'first_name', '2': 'last_name', '3': 'phone'}
            field_to_update = field_map.get(update_choice)
            
            if field_to_update:
                new_value = input(f"Enter new {field_to_update.replace('_', ' ')}: ")
                phonebook.update_contact(search_value, field_to_update, new_value)
            else:
                print("Invalid choice.")
                
        elif choice == '4':
            print("Search by:")
            print("1. First Name")
            print("2. Last Name")
            print("3. Phone Number")
            print("4. Any field")
            search_choice = input("Enter your choice (1-4): ")
            
            if search_choice in ['1', '2', '3', '4']:
                field_map = {'1': 'first_name', '2': 'last_name', '3': 'phone', '4': None}
                field = field_map.get(search_choice)
                
                search_term = input("Enter search term: ")
                contacts = phonebook.search_contacts(search_term, field)
                phonebook.display_contacts(contacts)
            else:
                print("Invalid choice.")
                
        elif choice == '5':
            contacts = phonebook.search_contacts()
            phonebook.display_contacts(contacts)
            
        elif choice == '6':
            search_value = input("Enter a name or phone number to delete: ")
            phonebook.delete_contact(search_value)
            
        elif choice == '7':
            phonebook.close_connection()
            print("Thank you for using PhoneBook!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main() 
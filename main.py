import data
import ui

# Retrieve all the address book data from database and store in persons array
data.retrieve_all_persons_from_db()
# Show main window of Address Book application
ui.show_address_book_window(data.persons)    

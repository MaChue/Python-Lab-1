import data
from tkinter import *
from tkinter import messagebox

# Show main window of Address Book Application
def show_address_book_window(persons: [data.Person], default_search_text=None):
  # Create a window
  root = Tk()             
  root.geometry('1000x500')
  root.title("Address Book Application")

  # Create a frame to embed search box, search button and add new contact button
  frame0 = Frame(root)
  frame0.grid(row=0, column=0)

  # Create Entry widget for search box
  search_text = StringVar(frame0)
  se = Entry(frame0, fg="black", textvariable=search_text) 
  # Place search box at row=0 and column=0 of frame0
  se.grid(row=0, column=0, padx=10, pady=20)
  if default_search_text != None:
    # Initialize text to the search box
    search_text.set(default_search_text)
  
  # Create search button at row=0 and column=2 of frame0 and perform search function when user click
  sb = Button(frame0, text='Search', fg='black', bg="lightgray", bd='1', command=lambda : search(root, search_text.get())) 
  sb.grid(row=0, column=2, padx=10, pady=20) 

  # Create add new contact button at row=0 and column=3 of frame0 and show Add Contact window when user click via show_add_or_edit_entry_window function
  ab = Button(frame0, text='Add New Contact', fg='black', bg="lightgray", bd='1', command=lambda : show_add_or_edit_entry_window(root)) 
  ab.grid(row=0, column=3, padx=10, pady=20) 

  # Create another frame to embed all the address list UI
  frame1 = Frame(root)
  frame1.grid(row=1, column=0)

  label_width = 15
  t_row = 0

  # Create Labels on frame1 that will show "Name", "Phone", "Email", "Company", "Address" title
  t0 = Label(frame1, width=3, fg='black', text='') 
  t0.grid(row=t_row, column=0) 
  t1 = Label(frame1, width=label_width, fg='black', text='Name') 
  t1.grid(row=t_row, column=1) 
  t2 = Label(frame1, width=label_width, fg='black', text='Phone') 
  t2.grid(row=t_row, column=2) 
  t3 = Label(frame1, width=label_width, fg='black', text='Email') 
  t3.grid(row=t_row, column=3) 
  t4 = Label(frame1, width=label_width, fg='black', text='Company') 
  t4.grid(row=t_row, column=4) 
  t5 = Label(frame1, width=label_width, fg='black', text='Address') 
  t5.grid(row=t_row, column=5)

  # Populate all the persons data that exit in the Address Book Database and show as Labels
  for i in range(len(persons)):
    e_row = i + 1
    person = persons[i]
    e0 = Label(frame1, width=3, fg='black', text=e_row) 
    e0.grid(row=e_row, column=0) 
    e1 = Label(frame1, width=label_width, fg='black', text=person.get_fullname()) 
    e1.grid(row=e_row, column=1) 
    e2 = Label(frame1, width=label_width, fg='black', text=person.phone) 
    e2.grid(row=e_row, column=2) 
    e3 = Label(frame1, width=label_width, fg='black', text=person.email) 
    e3.grid(row=e_row, column=3) 
    e4 = Label(frame1, width=label_width, fg='black', text=person.company) 
    e4.grid(row=e_row, column=4) 
    e5 = Label(frame1, width=label_width, fg='black', text=person.address) 
    e5.grid(row=e_row, column=5)
    # Create a button that will perform Edit function of the selected person
    e6 = Button(frame1, text='Edit', fg='green', bd='0', command=lambda p=person : show_add_or_edit_entry_window(root, p)) 
    e6.grid(row=e_row, column=6) 
    # Create a button that will perform Delete function of the selected person
    e7 = Button(frame1, text='Delete', fg='red', bd='0', command=lambda p=person : delete(root, p)) 
    e7.grid(row=e_row, column=7) 
  
  root.mainloop()
##############################################################

# The function that perform searching through person's name from the address book
def search(root, keyword: str):
  # Search person from the database
  persons = data.search_person_by_keyword(keyword)
  # Destory current window
  root.destroy()
  # Show it again with search result data
  show_address_book_window(persons, keyword)
##############################################################

# The function that perform deleting selected persons from the address book
def delete(root, person: data.Person):
  # Show confirmatio dialog before deleting
  msg_box = messagebox.askquestion('Confirmation','Are you sure you want to delete this contact?', icon='warning')
  if msg_box == 'yes':
    # If user click yes, delete the person from the database 
    persons = data.delete_person(person)
    # Distory the current window
    root.destroy()
    # Show again with current updated data
    show_address_book_window(persons)
##############################################################        

# The function that will show data entry popup on top of main window to perform add or edit functionalities
def show_add_or_edit_entry_window(root, person:data.Person=None):
  # Create a popup window that will display on top of main window
  popup = Toplevel(root)
  popup.geometry('300x450')

  # Declare variables that will store user input data through the Entry widgets
  first_name = StringVar(popup)
  last_name = StringVar(popup)
  phone = StringVar(popup)
  email = StringVar(popup)
  company = StringVar(popup)
  address = StringVar(popup)

  # If user open this window through Edit button, person data will not be None
  if person != None:
    # If person is not None, set person's data to these variables to show as text of Entry widgets
    first_name.set(person.first_name)
    last_name.set(person.last_name)
    phone.set(person.phone)
    email.set(person.email)
    company.set(person.company)
    address.set(person.address)
    popup.title("Edit Contact")
  else:
    popup.title("Add Contact")

  # Create a frame to embed Lables and Entry widgets
  frame1 = Frame(popup)
  frame1.pack(fill="both", expand=True)

  # Create Labels and Entry widgets to access user input  
  l1 = Label(frame1, fg="black", text="First Name:",  anchor="w") 
  l1.pack(fill="both", expand=True)
  e1 = Entry(frame1, fg="black", textvariable=first_name) 
  e1.pack(fill="both", expand=True)
  l2 = Label(frame1, fg="black", text="Last Name:",  anchor="w") 
  l2.pack(fill="both", expand=True)
  e2 = Entry(frame1, fg="black", textvariable=last_name) 
  e2.pack(fill="both", expand=True)
  l3 = Label(frame1, fg="black", text="Phone:",  anchor="w") 
  l3.pack(fill="both", expand=True)
  e3 = Entry(frame1, fg="black", textvariable=phone) 
  e3.pack(fill="both", expand=True)
  l4 = Label(frame1, fg="black", text="Email:",  anchor="w") 
  l4.pack(fill="both", expand=True)
  e4 = Entry(frame1, fg="black", textvariable=email) 
  e4.pack(fill="both", expand=True)
  l5 = Label(frame1, fg="black", text="Company:",  anchor="w") 
  l5.pack(fill="both", expand=True)
  e5 = Entry(frame1, fg="black", textvariable=company) 
  e5.pack(fill="both", expand=True)
  l6 = Label(frame1, fg="black", text="Address:",  anchor="w") 
  l6.pack(fill="both", expand=True)
  e6 = Entry(frame1, fg="black", textvariable=address) 
  e6.pack(fill="both", expand=True)

  # Create a frame to embed "Cancel" and "Save Changes" buttons
  frame2 = Frame(popup)
  frame2.pack(fill="both", expand=True)
  # Cancel button to cancle current operation and close current popup window
  b1 = Button(frame2, text='Cancel', fg='black', bg="lightgray", bd='1', command=popup.destroy) 
  b1.grid(row=0, column=0, padx=30, pady=20)
  # Save Changes button to comfirm current data changes and, update or add person data to database 
  b2 = Button(frame2, text='Save Changes', fg='white', bg="#848888", bd='1', command=lambda : add_or_edit_contact()) 
  b2.grid(row=0, column=1, padx=0, pady=20) 

  # The function to handle edit and add functionalities
  def add_or_edit_contact():
    # Check any of user input data is empty. If empty, show error messagebox.
    if len(first_name.get()) == 0 or len(last_name.get()) == 0 or len(phone.get()) == 0 or len(email.get()) == 0 or len(company.get()) == 0 or len(address.get()) == 0:
      messagebox.showerror("Invalid Entry!", "All data cannot be empty!", icon="error", parent=popup)
    else:
      if person != None:
        # If person is not None, perform edit function and show main window again with updated data
        person.first_name = first_name.get()
        person.last_name = last_name.get()
        person.phone = phone.get()
        person.email = email.get()
        person.company = company.get()
        person.address = address.get()
        persons = data.update_person(person)
        root.destroy()
        show_address_book_window(persons)        
      else:
        # If person is None, add new person to address book database and show main window again with updated data
        persons = data.add_new_person(first_name.get(), last_name.get(), phone.get(), email.get(), address.get(), company.get()) 
        root.destroy()
        show_address_book_window(persons)
##############################################################
from tkinter import *
import data
import ui


p1 = data.Person("John", "Smith", 6591034343, "johnsmith@gmail.com", "London, UK", "Amazon") 
p2 = data.Person("Susan", "Smith", 659603433, "susansmith@gmail.com", "London, UK", "Apple") 
p3 = data.Person("Amy", "Jame", 33534532432, "amyjame@gmail.com", "London, UK", "Google") 

data.add_new_person(p1)
data.add_new_person(p2)
data.add_new_person(p3)
for person in data.persons:
  print(person.get_fullname())
print("........................")

ui.show_address_book_window(data.persons)  # open the window with record at the starting        

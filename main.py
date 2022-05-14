import data

p1 = data.Person("John", "Smith", 6591034343, "johnsmith@gmail.com", "London, UK", "Amazon") 
p2 = data.Person("Susan", "Smith", 659603433, "susansmith@gmail.com", "London, UK", "Apple") 
p3 = data.Person("Amy", "Jame", 33534532432, "amyjame@gmail.com", "London, UK", "Google") 

data.add_new_person(p1)
data.add_new_person(p2)
data.add_new_person(p3)
for person in data.persons:
  print(person.get_fullname())
print("........................")

result = data.search_person_by_keyword("Smith")
for r in result:
  print(r.get_fullname())
print("........................")

#data.delete_person(1)
#for person in data.persons:
#  print(person.get_fullname())
#print("........................")

updated_person = data.Person("Zilly", "Smith", 659603433, "susansmith@gmail.com", "London, UK", "Google") 
data.update_person(updated_person, 0)
for person in data.persons:
  print(person.get_fullname())
print("........................")
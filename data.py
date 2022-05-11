class Person:
  'Class for abstract type of a person that will store in Address Book.'
  def __init__(self, first_name, last_name, phone, email, address, company):
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.email = email
    self.address = address
    self.company = company

  def get_fullname(self)-> str:
    return self.first_name + " " + self.last_name

# Array that will maintain list of Person objects shown in Address Book
persons = []

# Function to add new person to Address Book
def add_new_person(new_person: Person):
  if len(persons) == 0:
    persons.append(new_person)
  else:
    low = 0
    high = len(persons)
    while low < high:
      middle = (low + high) // 2
      if persons[middle].first_name.lower() < new_person.first_name.lower():
        low = middle + 1
      else:
        high = middle
    persons.insert(low, new_person)

# Function to delete person from Address Book 
def delete_person(index: int):
  if index >= 0 and index < len(persons):
    persons.pop(index)

# Function to search person by comparing with full name and inputed keyword
def search_person_by_keyword(keyword: str)->[Person]:
  result = []
  for person in persons:
    full_name = person.get_fullname().lower()
    try:
      person.get_fullname().lower().index(keyword.lower())
    except Exception as e:
      continue
    else :
      result.append(person)
  return result
  

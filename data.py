import sqlite3

class Person:
  'Class for abstract type of a person that will store in Address Book.'
  
  def __init__(self, id, first_name, last_name, phone, email, address, company):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.email = email
    self.address = address
    self.company = company

  def get_fullname(self)-> str:
    return self.first_name + " " + self.last_name
##############################################################

# Array that will maintain list of Person objects shown in Address Book
persons = []
# Database name that will store all the Address Book data
db_name = 'address_book.db'
##############################################################

# Function to add new person to Address Book
def add_new_person(first_name, last_name, phone, email, address, company)->[Person]:
  # Add new person to database
  new_person = add_new_person_to_db(first_name, last_name, phone, email, address, company)
  # Append new person to persons array and sorted by using binary insertion sort algorithm
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
  return persons
##############################################################

# Function to delete person from Address Book 
def delete_person(person: Person)->[Person]:
  # Delete person from database
  delete_person_from_db(person)
  index = get_index(person)
  # Delete person from persons array
  if index >= 0 and index < len(persons):
    persons.pop(index)
  return persons
##############################################################

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
##############################################################
  
# Function to update existing person data and sorted the array again
def update_person(person: Person)->[Person]:
  # Update person's data in the database
  update_person_to_db(person)
  index = get_index(person)
  # Update person data from the persons array and sort array with updated data by using insertion sort algorithm
  if index >= 0 and index < len(persons):
    persons[index] = person
    while index - 1 >= 0 and persons[index-1].first_name.lower() > persons[index].first_name.lower():
      temp = persons[index - 1]
      persons[index - 1] = persons[index]
      persons[index] = temp
      index = index - 1
    while index + 1 < len(persons) and persons[index + 1].first_name.lower() < persons[index].first_name.lower():
      temp = persons[index + 1]
      persons[index + 1] = persons[index]
      persons[index] = temp
      index = index + 1
  return persons
##############################################################

# Function to retrieve person object at index
def get_person(index: int)-> Person:
  if index >= 0 and index < len(persons):
    return persons[index]
  else:
    return None
##############################################################

# Function to retrieve index of person object
def get_index(person: Person)-> int:
  for index in range(len(persons)):
    if persons[index].id == person.id:
      return index
  else:
    return None
##############################################################

# Function to retrieve existing address book data from the database
def retrieve_all_persons_from_db()-> [Person]:
  # Create database connection
  conn = sqlite3.connect(db_name)
  
  # Check "Person" table is already exist in the address_book database
  listOfTables = conn.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='Person'; """).fetchall()
  
  if len(listOfTables) == 0:
    # If "Person" table is not exist, create "Person" table
    conn.execute('''CREATE TABLE Person
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name   TEXT       NOT NULL,
            last_name    TEXT       NOT NULL,
            phone        INT        NOT NULL,
            email        TEXT       NOT NULL,
            address      CHAR(50)   NOT NULL,
            company      TEXT       NOT NULL);''')
    print("Table created successfully")
  else:
    # If "Person" table is already exist, retrieve all the persons data from the database and store in "persons" array
    print("Person table exist")
    cursor = conn.execute('''SELECT id, first_name, last_name, phone, email, address, company 
                          FROM Person ORDER BY first_name, last_name;''')
    persons.clear()
    for row in cursor:
      person = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
      persons.append(person)
  conn.close()
##############################################################

# Function to add new person to database
def add_new_person_to_db(first_name, last_name, phone, email, address, company)-> Person:
  conn = sqlite3.connect(db_name)
  cursor = conn.execute('''INSERT INTO Person 
                (first_name, last_name, phone, email, address, company)
                VALUES (?, ?, ?, ?, ?, ?);''', (first_name, last_name, phone, email, address, company))
  id = cursor.lastrowid
  conn.commit()
  conn.close()
  return Person(id, first_name, last_name, phone, email, address, company)
##############################################################

# Function to update existing person from the database with new values
def update_person_to_db(person: Person):
  conn = sqlite3.connect(db_name)
  cursor = conn.execute('''UPDATE Person SET
                first_name=?, last_name=?, phone=?, email=?, address=?, company=?
                WHERE id=?;''', (person.first_name, person.last_name, person.phone, person.email, person.address, person.company,person.id))
  conn.commit()
  conn.close()
##############################################################

# Function to delete person from the database
def delete_person_from_db(person: Person):
  conn = sqlite3.connect(db_name)
  cursor = conn.execute("DELETE FROM Person WHERE id=?;", (person.id,))
  conn.commit()
  conn.close()
##############################################################
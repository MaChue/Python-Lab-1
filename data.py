class Person:
  'Class for abstract type of a person that will store in Address Book.'
  def __init__(self, first_name, last_name, phone, email, address, company):
    self.first_name = first_name
    self.last_name = last_name
    self.phone = phone
    self.email = email
    self.address = address
    self.company = company

  def get_fullname(self):
    return self.first_name + " " + self.last_name


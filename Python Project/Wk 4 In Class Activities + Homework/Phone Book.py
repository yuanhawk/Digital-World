phonebook = [{
  'name': 'Andrew',
  'mobile_phone': 9477865,
  'office_phone': 6612345,
  'email': 'andrew@sutd.edu.sg'
  }, {
  'name': 'Bobby',
  'mobile_phone': 8123498,
  'office_phone': 6654321,
  'email': 'bobby@sutd.edu.sg'
  }]

def get_details(name, key, lister):
  for user in lister:
    if user['name'] == name:
      return user.get(key)

customer = {
    "name":"John Smith",
    "age" : 30,
    "is_varified": True
}
print(customer)
print(customer['name'])
#print(customer['date'])
print(customer.get('name'))
print(customer.get('date', 'jan 1'))
print(customer)
customer['name'] = 'Jack Smith'
print(customer)
customer['Date'] = ''
print(customer)

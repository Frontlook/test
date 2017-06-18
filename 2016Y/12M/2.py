people = dict(Alice={
    'phone': '2341',
    'addr': 'Foo drive 23'
}, Beth={
    'phone': '1231',
    'addr': 'Bar street 42'
}, Ceil=dict(phone='2131', addr='Ceil street 83'))
labels = dict(phone='phone number', addr='address')
name = input('Name:')
request = input('Phone nunber (p) or address (a)?')
key=request
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'
person=people.get(name,{})
label=labels.get(key,key)
result=person.get(key,'not available')
print(name+'\'s '+label+result)
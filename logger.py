def write_contact(a):
    with open('phonebook.txt','a',encoding='utf-8') as f:
        f.write(a)

def read_contact():
    with open('phonebook.txt','r',encoding='utf-8') as f:
         return f.read()

def add_contact():
    name = input(" Введите имя: ")
    firstname = input(" Введите фамилию:")
    phone = input(" Введите номер телефона:")
    phonebook = name + " " + firstname +'||'+ phone +"\n"
    return phonebook

def find_contact(f):
        request = input(" Введите данные для поиска:")
        lst = list(filter(lambda x: request in x,f.split('\n') ))
        return lst
        


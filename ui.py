from model import add_contact,find_contact
from  logger import write_contact,read_contact

print('Выберите режим работы со справочником')
print('1.Запись абонента \n 2. Выведите справочник на экран\n 3. Поиск по справочнику')
choice = int(input())
if choice == 1: 
    a = add_contact()
    write_contact(a)

   
elif choice == 2:
    
    print(read_contact())
   
elif choice == 3:
   print(find_contact(read_contact()))
    
else: 
    print('Введено неверное значение')
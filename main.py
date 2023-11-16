#Field: Базовий клас для полів запису. Буде батьківським для всіх полів, у ньому реалізується логіка загальна для всіх полів
#Name: Клас для зберігання імені контакту. Обов'язкове поле.
#Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр). Необов'язкове поле з телефоном та таких один запис Record може містити декілька.
#Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів. Відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
#AddressBook: Клас для зберігання та управління записами. Успадковується від UserDict, та містить логіку пошуку за записами до цього класу


#Клас AddressBook:
# > OK  Реалізовано метод add_record, який додає запис до self.data.
# > Реалізовано метод find, який знаходить запис за ім'ям.
# > Реалізовано метод delete, який видаляє запис за ім'ям.
# > Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
#Клас Record:
# > OK Реалізовано зберігання об'єкта Name в окремому атрибуті.
# > OK Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
# > OK Реалізовано методи для додавання - add_phone
# > OK видалення - remove_phone
# > OK редагування - edit_phone
# > OK пошуку об'єктів Phone - find_phone.
#Клас Phone:
# OK > Реалізовано валідацію номера телефону (має бути 10 цифр).
#Реалізовано всі класи із завдання

from collections import UserDict
from colorama import init
init()

from collections import UserDict


    


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        
        if len(str(self.value)) == 10 and str(self.value).isdigit():
            self.value = value
        else:
            raise ValueError('Invalid phone number')
    
        


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        print(f'Create New Contact ===> Name: {self.name}')
    def add_phone(self,new_phone):
        self.phones.append(Phone(new_phone))
        print(f'Add new phone number: {new_phone}')
    def remove_phone(self,phone):
        for item in self.phones:
            if phone == item.value:
                print(f'Remove phone Number: {phone}')
                self.phones.remove(item)
                return
            
    def edit_phone(self,old_phone,new_phone):
        for item in self.phones:
            print(f'item => {item.value}: new_phone => {new_phone}: old_phone => {old_phone}')
            if item.value == old_phone:
                item.value = new_phone
                print(f'Edit Contact ===> old Contact: {old_phone} ===> new Contact{new_phone}')
                return
        raise ValueError()
    
    def find_phone(self,phone):
        for item in self.phones:
            if item.value == phone:
                print(f'Find {phone}')
                return item
        return None
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        print(f'Add record {record.name.value} ')
        self.data[record.name.value] = record
    def find(self, name):
        print(f'Find Name => {name}')
        print(self.data.get(name))
        return self.data.get(name)      
                
    def delete(self,name):

        if name in self.data:
            print(f'Delete {self.data[name]}')
            del(self.data[name])







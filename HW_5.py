# HW_5
# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
#     - как минимум один атрибут должен быть с уровнем доступа private.
#     Соответственно, для получения значений этого атрибута  нужно использовать методы get и set
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = 0  # Private атрибут для зарплаты

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Зарплата не может быть отрицательной")

    def introduce(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет, и я зарабатываю {self.get_salary()} $ в месяц.")

employee_1 = Employee("Alice Price", 30)   # экземпляр класса
employee_1.set_salary(5000)   # изменяем зарплату с помощью метода set_salary
employee_1.introduce()   # получаем зарплату с помощью метода get_salary и выводим информацию о человеке
employee_1.set_salary(-1000)    # попытка установить отрицательную зарплату
print(f"Зарплата {employee_1.name} сейчас: {employee_1.get_salary()} $.")   # получаем обновленную зарплату

class Intern(Employee):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def study(self):
        print(f"{self.name} учится в университете {self.university}")

class TopManager(Employee):
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company

    def work(self):
        print(f"{self.name} управляет компанией {self.company}")

intern_1 = Intern("Max Smith", 20, "High University")
topmanager_1 = TopManager("Bob Prince", 35, "ABC Corporation")

intern_1.introduce()
intern_1.study()

topmanager_1.set_salary(50000)
topmanager_1.introduce()
topmanager_1.work()

# 5.2. Создайте репозиторий на Github и отправьте файл с домашним заданием в этот удаленный репозиторий

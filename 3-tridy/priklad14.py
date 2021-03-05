class Employee:
    def get_info(self):
        return f"{self.name} pracuje na pozici {self.position}. Hrubou mrzu pobírá ve výši {self.salary} a má {self.children} dětí, čistá mzda je tedy {self.get_net_salary()}"

    def __init__(self, name, position, salary, children):
        self.name = name
        self.position = position
        self.salary = salary
        self.children = children

    def get_tax(self):
        tax = self.salary*0.15 - self.children*1500
        if tax < 0:
            tax = 0
        return tax

    def get_net_salary(self):
        net_salary = self.salary - self.get_tax()
        return net_salary


frantisek = Employee("František Novák", "Konstruktér", 15000, 0)
klara = Employee("Klára Nová", "Konstruktérka", 20000, 2)

print(frantisek.get_info())
print(klara.get_info())
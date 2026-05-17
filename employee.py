class employee :   
    name=input("Enter your name.")
    ID=input("Enter your ID.")
    department='Managment'
    salary="30,867"
    

    
    def ___init__(self):
        print("making a new employee entry")
    
    def show_detail(self):
        print("The details of employee are:")
        print(f'Name: {self.name}')
        print(f'ID: {self.ID}')
        print(f'department: {self.department}')
        print(f'salary: {self.salary}')
        
    def change_detail(self):
        print("\n\nPlease update your ID")
        self.ID=int(input())
        print("\nPlease change your name")
        self.name=input()
        print("\nDetails updated\n")


print('ID of employee:',employee.ID)


employee1=employee()
employee2=employee()


print()
employee1.show_detail()

employee1.change_detail()
print()

employee1.show_detail()
print()

employee2.show_detail()
print()

employee2.change_detail()
print()

employee2.show_detail()






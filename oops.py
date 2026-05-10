name=input("Enter your name.")
    age=12
    schoolclass='6th A'
    house="Sapphire"
    teacher='Mrs. Holland'

    #constructor- used to initionlize the class variables
    def ___init__(self):
        print("making a new student entry")
    
    def show_detail(self):
        print("The details of students are:")
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'School class: {self.schoolclass}')
        print(f'House: {self.house}')
        print(f'Teacher name: {self.teacher}')

    def change_detail(self):
        print("\n\nPlease update your age")
        self.age=int(input())
        print("\nPlease change your name")
        self.name=input()
        print("\nDetails updated\n")


print('Age of student:',student.age)

#creating an object
student1=student()
student2=student()

#calling functions to get details
print()
student1.show_detail()

student1.change_detail()
print()

student1.show_detail()
print()

student2.show_detail()
print()

student2.change_detail()
print()

student2.show_detail()






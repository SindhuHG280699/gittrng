class Employee:
    def __init__(self, empid, empname,empsal, empdept):
        self.empid= empid

        self.empname = empname

        self.empsal=empsal

        self.empdept = empdept

    def display(self):


         print('Name: ' self.empname)
         print('Empid:' self.empid)

         print('Empsal:' self.empsal)
         print('Empdept : 'self.empdept)

    def createtimesheet (self):
        date = input("enter date: ")
        noofhrs=input("enter noofhrs :")
        activity=input("enter activity:")
        description input("enter description: ")
        status = input ("enter status: ")

#TimeSheet date, no of hrs, activity, description, status

class Timesheet (Employee):
    def _init__(self, date, noofhrs,activity, description, status):

        Employee. __init__(self, self.empid, self.empname, self.empsal, self.empdept)

        self.date = date

        self.noofhrs = noofhrs
        self.activity = activity

        self.description = description

        self.status = status

e1=Employee('180', 'Ram', '35000', 'HR')
el.createtimesheet()

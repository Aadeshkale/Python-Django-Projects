import pymongo
from pymongo import MongoClient

try:
    client = MongoClient(host='localhost', port=27017)
    db = client.emp
    col = db.empinfo

except Exception as e:
        print(e)

def show():

        res = col.find()
        print('--' * 100)
        for x in res:
            print(x)
            print('--' * 100)
        menu()
def search():
      name=input('Enter first name of employee:')
      res=col.find({'name.first':name})
      print('--' * 100)
      for x in res:
          print(x)
      print('--' * 100)
      menu()

def insert():
    s={
        'name':{
            'first':'test',
            'last':'test'
        },
        'age':00,
        'salary':00,
        'address':{
            'location':'none',
            'city':'none',
            'state':'none'
        }
    }
    namef=input('Enter First Name of employee:')
    namel = input('Enter Last Name of employee:')
    age = input('Enter age of employee')
    salary=input('Enter salary of employee:')
    location=input('Enter the address of employee:')
    city=input('Enter city of employee:')
    state=input('Enter state of employee:')
    s['name']['first'] = namef
    s['name']['last'] = namel
    s['age']=age
    s['salary']=salary
    s['address']['location']=location
    s['address']['city']=city
    s['address']['state']=state
    db.empinfo.insert(s)
    print('Employee record inserted successfully :)')
    menu()

def dele():
    namef = input('Enter First Name of employee:')
    col.empinfo.remove({'name.first':namef})
    print('Employee record removed successfully :)')
    menu()

def update():
    namef = input('Enter First Name of employee:')
    namel = input('Enter Last Name of employee:')
    age = input('Enter new age of employee:')
    salary = input('Enter new salary of employee:')
    location = input('Enter new address of employee:')
    city = input('Enter new city of employee:')
    state = input('Enter new state of employee:')
    db.empinfo.update({'name.first':namef,'name.last':namel},{ '$set':{
      'age':age,
      'salary':salary,
          'address':{
              'loacation':location,
              'city' :city,
              'state':state
          }
    }})
    print('Employee record Updated successfully :)')
    menu()

def menu():
    print('**' * 26)
    print("1.Show All Employee \n2.Search Employee \n3.Insert Employee \n4.Remove Employee\n5.Update Employee \n6.exit ")
    print('**' * 26)
    ch = input('Enter Ur Choice:')
    if ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6':
        if ch == '1':
            show()

        elif ch=='2':
           search()

        elif ch=='3':
            insert()

        elif ch=='4':
            dele()
        elif ch=='5':
            update()

        elif ch == '6':
            exit()
            client.close()
    else:
        print('Please Enter valid choice :(')
menu()
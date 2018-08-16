import mysql.connector
flag=False # for to decide when we execute delete , insert query
def connectivity(sql):
    try:
        con = mysql.connector.connect(host='localhost', database='sample', user='root', password='dx619')
        cursor=con.cursor()
        cursor.execute(sql)

        if flag==True:
            con.commit()                         # to commit changes in the database
            cursor.execute('select * from emp')  # when we perform delete , insert operation  fetchall() does't fetch any data

        data=cursor.fetchall()
        print('--' * 26)
        for id,name,gender,age,salary,address in data:
            print(id,'|',name,'|',gender,'|',age,'|',salary,'|',address)
            print('--'*26)
        cursor.close()

        menu()               # calling menu to for continue loop
    except Exception as e:
        print('Exception has occured'+e)

# main-menu

def menu():
        print('*' * 22)
        print(
            ' 1.Show All Employee\n 2.Search Employee \n 3.Insert New Employee  \n 4.Delete Employee \n 5.Update Employee \n 6.exit')
        print('*' * 22)

        ch = input('Enter ur Choice:')
        if ch == '1'  or ch == '2' or ch == '3' or ch == '4' or ch=='5' or ch=='6':
            if ch=='1' :
                connectivity('select * from emp')
            elif ch=='2':
                idt=input("Enter employee Id:")
                connectivity('select * from emp where id = {}'.format(idt))
            elif ch=='3':
                 flag=True
                 idt=input('Enter new Employee id:')
                 namet = input('Enter new Employee name:')
                 gendert = input('Enter new Employee gender:')
                 aget=input('Enter new Employee age:')
                 salaryt=input('Enter new Employee salary:')
                 addresst = input('Enter new Employee address:')

                 connectivity("insert into emp values ({},'{}','{}',{},{},'{}')".format(idt,namet,gendert,aget,salaryt,addresst))

            elif ch=='4':
                flag = True
                idt=input('Enter Id of Employee you want to delete:')
                connectivity('delete from emp where id = {}'.format(idt))

            elif ch=='5':
                flag = True
                idt = input('Enter Employee id:')
                namet = input('Enter new Employee name:')
                gendert = input('Enter new Employee gender:')
                aget = input('Enter new Employee age:')
                salaryt = input('Enter new Employee salary:')
                addresst = input('Enter new Employee address:')

                connectivity("update emp set name='{}',gender='{}',age={},salary={},address='{}' where id={}".format(namet,gendert,aget,salaryt,addresst,idt))
            elif ch=='6':
                exit()

        else:
            print('Please Enter valid choice :( ')
menu()


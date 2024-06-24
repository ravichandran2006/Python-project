import mysql.connector as mysql
db=mysql.connect(host="localhost",user="root",password="",database="geek")
command_handler = db.cursor(buffered=True)
def teacher_session():
    print("Login Successful !! Welcome Teacher")
    while 1:
        print("")
        print("Teacher's Menu")
        print("1.Mark student register")
        print("2. View Register")
        print("3.Logout")
        user_option = input(str("option : "))
        if user_option == "1":
            print("")
            print("Mark Student register")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")        
            records=command_handler.fetchall()
            date=input(str("Date : DD/MM/YYY :"))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",","")
                record = str(record).replace("(","")                
                record = str(record).replace(")","")
                status = input(str("Status For " + str(record) + " p/A/L : "  ))
                query_vals=(str(record),date,status)
                command_handler.execute("INSERT INTO attendance(username,date,status) VALUES(%s,%s,%s)",query_vals)
                db.commit()
                print(record + "Marked as" + status)
        elif user_option=="2":
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username,date,status FROM attendance")
            records =command_handler.fetchall()
            print("Displaying All registers")
            for record in records:
                print(record)
        elif user_option=="3":
            break
        else:
            print("No valid options are selected")
def student_session():
    while 1:
        print("")
        print("1.View Register")
        print("2.Download register")
        print("3.Logout")
        user_option =input(str("option : "))
        if user_option == "1":
            username = (str(username))
            command_handler.execute("SELECT date,username,status FROM attendance WHERE username=%s",username)
            records=command_handler.fetchall()
            for record in records:
                print(record)

def admin_session():
    print("Login Successful !! Welcome Admin")
    while 1:
        print("")
        print("Admin Menu")
        print("1.Register New Student")
        print("2.Register Teacher")
        print("3.Delete Existing Student")
        print("4.Delete Existing Teacher")
        print("5.Log out")

        user_option=input(str("option: "))
        if user_option == "1":
            print("")
            print("Register New Student")
            username= input(str("Student Username : "))
            password= input(str("Student Password :"))
            query_vals=(username,password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES(%s,%s,'student')",query_vals)
            db.commit()
            print(username + " has been registered as a Student")
        elif user_option == "2":
            print("")
            print("Register New Teacher")
            username= input(str("Teacher Username : "))
            password= input(str("Teacher Password :"))
            query_vals=(username,password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES(%s,%s,'Teacher')",query_vals)
            db.commit()
            print(username + " has been registered as Teacher")
        elif user_option =="3":
            print("")
            print("Delete Exisiting Student Account")
            username= input(str("Student Username : "))
          
            query_vals=(username,"student")
            command_handler.execute("DELETE FROM users WHERE username=%s AND privilege=%s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")
        elif  user_option == "4":
            print("")
            print("Delete Exisiting Teacher Account")
            username= input(str("Teacher Username : "))
          
            query_vals=(username,"teacher")
            command_handler.execute("DELETE FROM users WHERE username=%s AND privilege=%s ",query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")
        elif user_option == "5":
            break
        else:
            print("No valid options are selected")
def auth_student():
    print("")
    print("Student's Login")
    print("")
    username=input(str("Username: "))
    password=input(str("password: "))
    query_vals=(username,password,"student")
    command_handler.execute("SELECT username FROM users WHERE username =%s AND password= %s AND privilege=%s",query_vals)    
   
   
    if command_handler.rowcount <=0:
        print("Invalid Login Details")
    else:
        student_session()
def auth_teacher():
    print("")
    print("Teacher's Login")
    username=input(str("Username: "))
    password=input(str("password: "))
    query_vals=(username,password)
    command_handler.execute("SELECT * FROM users WHERE username= %s AND password = %s AND privilege='teacher'",query_vals)
    if command_handler.rowcount<=0:
        print("Login not recognized")
    else:
        print("Welcome Teacher !!")
        teacher_session()
            

    
def auth_admin():
    print("")
    print("Admin login")
    print("")
    username=input(str("Username: "))
    password=input(str("password: "))
    if username == "rithik":
        if password =="password":
            admin_session()
        else:
            print("Incorrect Username or Password")
    else:
        print("Login details are not recognised")


def main():
    while 1:
        print("Welcome to college management System")
        print("")
        print("1.Login as student")
        print("2.Login as teacher")
        print("3.Login as admin")
        
        user_option = input(str("option: "))
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_teacher()
        elif user_option == "3":
            auth_admin()
        else:
            print("No valid option was selected")
main()

            
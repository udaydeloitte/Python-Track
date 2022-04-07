from Main_assignment.Admin import adminLogin
from Main_assignment.UserRegistration import register

obj_register = register()
print("******Welcome To BookMyShow******* ")
obj_Admin = adminLogin()

while True:
    print("Press 1 to login as admin: ")
    print("Press 2 to register: ")
    print("Press 3 to login as user")
    print("Press 4 to exit")
    user_input = input()
    if user_input == "4":
        break
    elif user_input == "1":
        if obj_Admin.login_admin():
            print("Login Successful! ")
            print()
            print("******Welcome Admin******* ")
            while True:
                print("Press 1 to add movie info. ")
                print("Press 2 to Edit movie info. ")
                print("Press 3 to Delete movie ")
                print("Press 4 to Logout")
                admin_input = input()
                if admin_input == "4":
                    break
                elif admin_input == "1":
                    obj_Admin.addMovie()
                elif admin_input == "2":
                    obj_Admin.EditMovie()
                else:
                    obj_Admin.deleteMovie()
        else:
            print("Invalid Credentials")
    elif user_input == "2":
        if obj_register.userregister():
            print()
            pass
        else:
            continue
    elif user_input == "3":
        if obj_register.userlogin():
            print()
            obj_register.movies()
        else:
            continue
    else:
        print("Invalid Input ")
        continue

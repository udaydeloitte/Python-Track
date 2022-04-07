from Main_assignment.Admin import adminLogin

print("******Welcome To BookMyShow******* ")
obj_Admin=adminLogin()
while True:
        print("Press 1 to login: ")
        print("Press 2 to register: ")
        print("Press 3 to exit")
        user_input=input()
        if user_input=="3":
            break
        elif user_input=="1":
            if obj_Admin.login_admin():
                print("Login Successful! ")
                print()
                print("******Welcome Admin******* ")
                while True:
                    print("Press 1 to add movie info. ")
                    print("Press 2 to Edit movie info. ")
                    print("Press 3 to Delete movies ")
                    print("Press 4 to Logout")
                    admin_input=input()
                    if admin_input=="4":
                        break
                    elif admin_input=="1":
                        obj_Admin.addMovie()
                    elif admin_input=="2":
                        obj_Admin.EditMovie()
                    else:
                        obj_Admin.deleteMovie()
            else:
                print("Invalid Credentials")
        else:
            print("Wrong Input ")
            continue



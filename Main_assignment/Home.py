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
        else:
            continue
    elif user_input == "3":
        if obj_register.userlogin():
            print()
            while True:
                obj_register.movies()
                print("Enter Movie ID")
                print("Enter 0 to logout")
                choice=input()
                if choice=="0":
                    break
                else:
                    obj_register.movieInfo(int(choice))
                    print()
                    print("Press 1 to Book Tickets")
                    print("Press 2 to Cancel Tickets")
                    print("Press 3 for user ratings")
                    userChoice=input()
                    if userChoice=="2":
                        obj_register.cancelTickets(int(choice))
                    elif userChoice=="3":
                        obj_register.Userratings(int(choice))
                    else:
                        print("Enter valid input!")
        else:
            continue
    else:
        print("Invalid Input ")
        continue

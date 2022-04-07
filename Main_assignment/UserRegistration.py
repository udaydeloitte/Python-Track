from openpyxl import load_workbook


class register:
    def userregister(self):
            username = input('Enter username: ')
            if username in open('register.txt', 'r').read():
                print('Username already exists')
                return False
            password = input('Enter password: ')
            c_password = input('Enter confirm password: ')
            if password != c_password:
                print('password did not match')
                return False
            file = open('register.txt', 'a')
            file.write(username)
            file.write(' ')
            file.write(password)
            file.write('\n')
            file.close()
            print('You are successfully registered ')
            return True

    def userlogin(self):
        print("****Login to BookMyShow: ****")
        username = input('Enter registered username: ')
        password = input('Enter registered password: ')
        get_data = open('register.txt', 'r').readlines()
        users_data = []
        for user in get_data:
            users_data.append(user.split())

        total_user = len(users_data)
        increment = 0
        login_success = 0
        while increment < total_user:
            usernames = users_data[increment][0]
            passwords = users_data[increment][1]
            if username == usernames and password == passwords:
                login_success = 1
            increment += 1

        if login_success == 1:
            print("Login Successful Welcome",username)
            return True
        else:
            print('invalid username or password ')
            return False

    def movies(self):
        print("*** Movies List ***")
        wb = load_workbook("tim.xlsx")
        ws = wb.active
        rows = len(list(ws.rows))
        range = ws["A1":"A" + str(rows)]
        for movie in range:
            for x in movie:
                print(x.value)
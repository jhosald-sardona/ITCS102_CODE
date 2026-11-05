from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Enter the username")
    password = getpass("Enter the Password")

    if username == "andoy1" and password == "andoypogi123":
        print("access granted")
        isLogin = True
    else:
        print("access denied")
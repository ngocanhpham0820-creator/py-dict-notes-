dict={
    "user1":"1111",
    "user2":"2222",
    "user3":"3333",
    "user4":"4444",
    "user5":"5555",
    "user6":"6666",
    "user7":"7777",
    "user8":"8888",
    "user9":"9999",
    "user10":"9999",
}
while True:
    username = input("Enter your username: ")
    if username in dict:
        password = input("Enter your password: ")
        if password == dict[username]:
            print("You are logged in")
            break
        else:
            print("Wrong password")
            break
    else:
        print("Wrong username")

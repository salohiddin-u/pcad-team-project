# unique id
# import random
#
# users_base = {}
# id_base = []
# users_package_id =[]
#
#
# for i in range (1, 20):
#     while True:
#         ran_checker = random.randint(1, 20)
#         if ran_checker not in id_base:
#             id_base.append(ran_checker)
#             break
#     print(ran_checker)
#
# print(f"\nYour Package is ready {id_base}")
import sys
import time

#db

users_db ={'Alex': '923',
           'Mark': '1203012jiijfe'}

print(f"{'*' * 5} kinda AMAZON but that one really works in Uzbekistan {'*' * 5}")

while True:
    print("\t1. Enter as a user\n"
          "\t2. Create an account\n"
          "\t0. Exit")

    signing_up = input('CHOICE: ')
    match signing_up:
        case '1':
            while True:

                username = input("Enter your username: ")
                if username not in users_db:
                    print(f"Username {username} is not exists please try to create a new account"
                          f"/ try something with different Capital words")
                    continue
                password = input("Enter your password: ")
                if users_db[username] == password:
                    print("Welcome back")
                    print("\t1. Make an order\n"
                          "\t2. Track orders\n"
                          "\t3. Orders\n"
                          "\t0. Quit")
                    choice = input('CHOICE: ')
                    match choice:
                        case '0':
                            print('Bye!')
                            break
                else:
                    print("Wrong password or username", file=sys.stderr)
                    time.sleep(0.1)


        case '2':
            while True:
                username = input("Enter new username: ")
                if username in users_db:
                    print(f"Username {username} is already exist please try one more time")
                    continue
                else:
                    password = input("Enter new password: ")
                    users_db[username] = password
                    print("You have signed successfully")
                    print("\t1. See orders\n"
                          "\t2. Order home stuff\n"
                          "\t3. ")
                    choice = input('CHOICE: ')
                    match choice:
                        case '0':
                            print('Bye!')
                            break


        case '0':
            print('Bye!')
            break


        case '101209':
            print("you have entered as an admin: ")
            print(users_db)



        case _:
            print("try again ")






























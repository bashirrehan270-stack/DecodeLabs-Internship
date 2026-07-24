# Password Generator
import random


class password_generator:
    def __init__(self):
        self.lower = "abcdefghigklmnopqrstuvwxyz"
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.number = "0123456789"
        self.symbol = "!@#$%&*,.?|"
        self.record = []

    def generate_password(self, lenght, use_number, use_symbol):
        final_item_password = self.lower + self.upper

        if use_number == "y":
            final_item_password += self.number
        if use_symbol == "y":
            final_item_password += self.symbol

        password = "".join(
            random.choice(final_item_password) for _ in range(lenght)
            )

        self.record.append(password)
        return password

    def view_previous_password(self):
        if not self.record:
            print("No password build!")
        else:
            for password in self.record:
                print(password)


tracker = password_generator()
while True:
    print("=====Password Generator====")
    print("1.Generate a new password:")
    print("2.View previous password:")
    print("3.Exit")

    chose = input("Enter our choice: ")

    if chose == "1":
        lenght = int(input("Enter the pasword lenght: "))
        use_num = input("Number use in password(y/n):").strip().lower()
        use_sym = input("Symbol use in password(y/n):").strip().lower()
        how_many = int(input("How many password you want to generate?"))
        for i in range(how_many):
            new_password = tracker.generate_password(lenght, use_num, use_sym)
            print(f"{i+1}: {new_password}")
    elif chose == "2":
        for password in tracker.record:
            print(password)
    elif chose == '3':
        print("closing...")
        break
    else:
        print("Invalid number!")

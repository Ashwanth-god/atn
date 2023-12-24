# atm code
import sys

import mysql.connector
from datetime import datetime as dt

# database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="ashwanth_atm"
)

# welcome message
print("welcome to ashwanth's atm machine")
cursor = db.cursor()


# class's coding starts
class function:
    # creating self variables

    def __init__(self):
        self.pin_entering = int(input("Enter pin:"))

        sql1 = "select * from data1 where pin = %s"
        val1 = self.pin_entering
        cursor.execute(sql1, (val1,))

        result = cursor.fetchall()

        for a1234 in result:
            if a1234 != -1234:
                self.id = a1234[0]
                self.balance = a1234[1]
                self.pin = a1234[2]
                self.name = a1234[3]

        db.commit()

    # withdraw method
    def withdraw(self):
        balance = self.balance

        wana_with = int(input("Hello, how much money you want to withdraw:\n"))
        if wana_with > self.balance:
            print("invalid amount")
            self.withdraw()

        else:
            ans1 = balance - wana_with
            to = dt.now()
            file1 = open("receipt.txt", "a")
            file1.write("            ashwanth's atm            ")
            file1.write("\n")
            file1.write("\n")
            file1.write("withdrawn by(name)                 :  ")
            file1.write(str(self.name))
            file1.write("\n")
            file1.write("time of withdrawal                 :  ")
            file1.write(str(to))
            file1.write("\n")
            file1.write("\n")
            file1.write("Total money before withdrawal      :  ")
            file1.write(str(self.balance))
            file1.write("\n")
            file1.write("Money withdrawn now                :  ")
            file1.write(str(wana_with))
            file1.write("\n")
            file1.write("Money  now available for withdraw  :  ")
            file1.write(str(ans1))
            file1.close()

            sql = "update data1 set balance = %s where pin = %s"
            val = (ans1, self.pin)
            cursor.execute(sql, val)

            db.commit()

            print("Please collect your money")
            print("Your receipt is in a text file called 'receipt.txt' ")

            do_not_know_a_name = input("do you want to use again, please type 'yes', else 'no'")
            if do_not_know_a_name.lower() == "yes":
                main_code(self.pin_entering)
            else:
                print("thank you, have a nice day")
                a123 = input("Press any key to exit")
                if a123:
                    sys.exit()

    # balance method
    def balance_me(self):
        print("Hello")
        print("your current account balance is ", self.balance)
        a1 = input("if you want to withdraw money, please type yes , else type no")
        if a1.lower() == "yes":
            self.withdraw()
        else:
            print("thank you, have a nice day")

    # pin_changing method
    def pin_changing(self):
        print("Hello, please enter your old pin code")
        pin_new = int(input(""))
        if pin_new == self.pin:
            print("please enter your new pin code")
            b = int(input(""))
            if pin_new == b:
                print("sorry, your old pin can't be your new pin")
            elif pin_new != b:
                sql = "update data1 set pin = %s where balance = %s"
                val = (b, self.balance)
                cursor.execute(sql, val)

                db.commit()

        else:
            print("Please, try again")


# class's coding ends


# object creating
a = function()

# check function
def check(op):
    if "1" == op:
        a.withdraw()
    elif "2" == op:
        a.balance_me()
    elif "3" == op:
        a.pin_changing()
    else:
        print("please try again")
        main_code(a.pin_entering)


def main_code(pin1):
    try:
        if pin1 == a.pin:
            dict1 = {1: "withdraw money", 2: "balance", 3: "change pin number"}
            for x, y, in dict1.items():
                print(x, y)
            op = str(input("Enter the operation you want to perform:"))
            check(op)
    except AttributeError:
        print("Account with this pin is not founded, please try again")

    else:
        pass


main_code(a.pin_entering)

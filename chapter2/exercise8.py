"""Write a Python program to solve the general version of the above problem. Ask the user for the time now(in hours),
and ask for the number of hours to wait. Your program should output what time will be on the clock when the alarm goes off."""


def main():
    time = int(input("Enter current time: "))
    alarm = int(input("How many hour you want to wait: "))
    future_hour= alarm % 24
    print((future_hour + time) % 12)
main()
"""The formula for computing the final amount if one is earning interest is given on Wikipedia as 

    A = P(1+r/n)**nt

    P= principal amount (initial investment)
    r = annual nominal interest rate (as a decimal)
    n = number of times the interest is compounted per year
    t = number of year

write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value of 12, and assign to r the
interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for.
Calculate and print the final amount after t years.

"""

def main():
    t = int(input("Enter years: "))
    p = 10000
    n = 12
    r = 8 / 100
    a = p * (1+r/n)**(n*t)
    print("Final amount is: ", a)
main()
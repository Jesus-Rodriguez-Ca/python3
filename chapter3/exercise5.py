"""Asume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

a) Write a loop that prints each of the numbers on a new line
b) Write a loop that prints each number and its square on a new line
c) Write a loop that adds all the numbers from the list into a variable called total. You should set the variable total
   to have the value 0 before start adding them up, and print the value in total after the loop has copmpleted
d) Print the product of all the numbers in the list. (product means all multiplied together)

"""

def main():
    xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
    total = 0
    product = 1
    print("a)")
    print("---------------------------------------------")

    for i in xs:
        print(i)

    print("b)")
    print("---------------------------------------------")
    for i in xs:
        print(i**2)

    print("c)")
    print("---------------------------------------------")
    for i in xs:
        total = total + i
    print("The sum of all the number is:", total)

    print("d)")
    print("---------------------------------------------")

    for i in xs:
        product = product * i
    print("The product of all the numbers is: ", product)


main()
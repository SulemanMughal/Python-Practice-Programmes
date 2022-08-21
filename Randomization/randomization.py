from random import *
import turtle

def main():

    print("\n>>>>>>>>>>Random Turtle Image<<<<<<<<<<\n")
    nmb1=int(input("Enter the start number: "))
    nmb2=int(input("Enter the second number: "))
    nmb3=int(input("Enter the third number: "))
    nmb4=int(input("Enter the fourth number: "))
    turtle.forward(nmb1)
    turtle.left(90)
    turtle.forward(nmb2)
    turtle.left(90)
    turtle.forward(nmb3)
    turtle.left(90)
    turtle.forward(nmb4)
    turtle.left(90)


if __name__ == "__main__":
    main()
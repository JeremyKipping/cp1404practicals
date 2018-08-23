"""

CP1404/CP5632 - Practical

 for temperature conversion

"""



MENU = """C - Convert Celsius to Fahrenheit

F - Convert Fahrenheit to Celsius

Q - Quit"""


print(MENU)
def main():
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius_to_fahrenheit(choice)
            print(MENU)
            choice = input(">>> ").upper()

        elif choice == "F":
            fahrenheit_to_celsius(choice)
            print(MENU)
            choice = input(">>> ").upper()

        else:
             print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
    print("Thank you.")



def celsius_to_fahrenheit(choice):
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))

def fahrenheit_to_celsius(choice):
    fahrenheit = float(input("Celsius: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} F".format(celsius))


main()
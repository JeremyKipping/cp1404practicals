

#files program 1
out_file = open("name.txt", "w")
name = input("What is you're name? ")
print(name, file=out_file)
out_file.close()

#files program 2
in_file = open("name.txt", "r")
name = in_file.read()
print("You're name is", name)
in_file.close()

#files program 3
in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

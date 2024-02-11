# დავალება1
#
print("Task 1")
print("Enter 3 integer numbers")
Number1 = int(input("Enter Number1:"))
Number2 = int(input("Enter Number2:"))
Number3 = int(input("Enter Number3:"))
sum = Number1 + Number2 + Number3
print ("The sum of 3 numbers is: ", sum)

# დავალება2
# კუბის გვერდი = a
print("Task 2")
a = int(input("Enter the length of a Cube's edge:"))
v = a ** 3
s = 6 * (a ** 2)
print("Volume of your cube is:",v)
print("Surface of your cube is:",s)

# დავალება3
print("Task 3")
Monitor_Price = int(input("Enter price of the Monitor: "))
SystemBlock_Price = int(input("Enter price of the System block:"))
Keyboard_Price = int(input("Enter price of the Keyboard:"))
Mouse_Price = int(input("Enter price of the Mouse:"))

Computer_Price = Monitor_Price+SystemBlock_Price+Mouse_Price+Keyboard_Price

print(f"Total price of your computer is {Computer_Price}")
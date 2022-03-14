#Ask user for name
name = input("What is your name?: " )

#ask user for age
age = int(input("How old are you?: "))

#Ask user for city
city = input("Where do you live?: ")

#Ask user what they enjoy
love = input("What do you love doing?: ")

#Create Outpt Text
string = "Your name is {} and you are {} years old. You live in {} and you love {}."
output = string.format(name,age,city,love)

#Print output to screen
print(output)

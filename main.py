# PRINTING HELLO WORLD
print("hello world")

# MAKING VARTIABLES
age = 21
is_adult = True

# TAKING INPUT ///////////////////////////////////////
# name = input("What is your name?\n")

# print ("Hello " + name )

# CHANGING DATA TYPE /////////////////////////////////
# age = int(input("What is your age ? \n"))

# print("You are "+str(age) +" years old")

#WORKING WITH STRING //////////////////////////////////
# name = "Tony Stark"
# print(name.upper()) # Convert into uppercase, 
# print(name.find("Stark")) # Returns the starting index (starts from 0)
# print(name.replace("Tony Stark", "Ironman")) # Replace and return
# print('S' in name) # Returns True if 'S' exists in 'name'  else returns 'false'

# # tHIS DOES NOT CHANGE THE MAIN STRING
# print(name)


# # MATHEMATICAL OPERATORS ///////////////////////////////
# print(2+3) # Addition
# print(3-1) # Subtraction
# print(2*3) # Multiplication
# print(2/3) # Division
# print(2//3) # Returns the integer part after division
# print(2%3) # Returns the remender part after division

# # LOGICAL OPERATORS ////////////////////////////////////
# print(2>3  or 5>3) # Returns true if one condition id true
# print(2>3  and 5>3) # Returns true if both condition id true
# print(not 5>3) # Reverses the condition return

# # IF ELSE STATEMENT
# age = 21
# if age >= 18: # no need to use {}, use :
#     print("You are an adult") # We use indentation to define a block of code
#     print("You can vote now")

# elif  age < 18 and age >3:
#     print("You are teen ager")

# else: 
#     print("You are a kid")



# BUILDING A SIMPLE CLCULATOR USING IF/ELSE ////////////////
# first = float(input("Enter the first number: "))
# operator = input("Enter the operator (+, -, /, *, %): ")
# second = float(input("Enter the second  number: "))

# if operator == '+':
#     print(first + second)
# elif operator == '-':
#     print(first - second)
# elif operator == '/':
#     print(first / second)
# elif operator == '*':
#     print(first * second)
# elif operator == '%':
#     print(first % second)
# else: 
#     print("Wrong input")

# LOOPS IN PYTHON (WHILE LOOP) ///////////////////////////////
i=1
while i <= 10:
    print(i  * '*')
    i += 1

# FOR LOOP ///////////////////////////////////////////////////

for j in range(10): # FOR EVERY j IN RANGE OF 0-9 
    print(j) # WILL PRINT 0,1,2,3,.....,9 


print(3 in range(8)) # RETURNS TRUE IF 3 IS BETWEEN 0-7 OR 0-(1-8)

# LIST IN PYTHON ////////////////////////////////////////////
marks = [20,54,47,64]
print(marks) # PRINTS THE ARRAY 'marks'
print(marks[2]) # PRINTS THE 3rd ELEMENT OF 'marks'. BESAUSE PYTHON STARTS THE INDEX FROM 0
print(marks[-1]) # PRINTS THE LAST ELEMENT, IF IT'S [-2], IT WILL PRINT 2nd LAST AND SO ON
print(marks[0:3]) # PRINTS THE ELEMENT 0,1 AND 2 

# APPENDING OR ADDING NEW DATA IN THE LIST
marks.append(45)
print(marks)

marks.insert(0,32) # WILL INSERT OR ADD 32 AT 0th INDEX OF 'marks' AND UPDATE IT
print(marks)

# PRINTING DATA USING FOR LOOP
for i in marks:
    print(i)

marks.clear() # WILL CLEAR THE LIST
print(marks)


# BREAK AND CONTINUE //////////////////////////////////////////
name = ["sohail", "rocky", "alamin", "izaz"]
for i in name:
    if i == "alamin":
        break # IF NAME IS "alamin", LOOP WILL BE EXIT

    print(i)

print("//////////////////////////////////////////////")

for j in name:
    if j == "alamin":
        continue # WILL SKIP THE NAME "alamin" AND CONTINUE THE EXECUTION

    print(j)
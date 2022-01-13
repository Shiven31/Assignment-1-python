
#Question Number 1
print("#Question Number 1") 
X= input("Input your First Number= ")
Y= input("Input your Second Number= ")
Z= input("Input your Third Number= ")
Average = (int(X)+int(Y)+int(Z))/3
print("The Average of your Three Numbers = ", Average) 

#Question Number 2
print("#Question Number 2")
X = float(input("Input your Gross Income= "))
Y = int(input("Input the number of Dependents= "))
A = (X-10000-(3000*Y))
B = A*0.2

#Question Number 3
print("#Question Number 3")
 
# Taking inputs for the list

SID = int(input('Enter Your SID:  '))
Name = str(input('Enter Your Name:  '))
Cgpa = float(input('Enter Your CGPA:  '))
Gender = str(input('Enter Your Gender:  '))
Course_Name = str(input('Enter Your Course name:  '))

# Creating the list
My_List = [SID , Name , Cgpa , Gender , Course_Name]

# Display result
print('Student',My_List)
print("Income Tax you have to pay = ", B)

#Question Number 4
print("#Question Number 4")

# Taking input of marks
M1 = int(input("Marks of The 1st student : "))
M2 = int(input("Marks of The 2nd student : "))
M3 = int(input("Marks of The 3rd student : "))
M4 = int(input("Marks of The 4th student : "))
M5 = int(input("Marks of The 5th student : "))

# Creating the list
Sorted_Marks = [M1, M2, M3, M4, M5]

# Applying the operation required
Sorted_Marks.sort()

# Display result
print(Sorted_Marks)


#Question Number 5(A)
print("#Question Number 5(A)") 
# Creating the list of Colours
List_colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Applying the operation asked in Question to remove 4th colour.
List_colors.pop(3)

#Printing the Result
print('Colors', List_colors)

#Question Number 5(B)
print("#Question Number 5(B)")

# Applying the operations
List_colors.pop(3)
List_colors.append('purple')

#Printing the Result
print('Colors', List_colors)




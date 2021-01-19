a = int(input("Enter First Number: ")) #Taking our First Number as input.
b = int(input("Enter Second Number: ")) #Taking our Second Number as input.

print('''Enter your choice:
Enter 1 for Addition.
Enter 2 for Subtraction.
Enter 3 for Multiplication.
Enter 4 for Division.''') # Giving instructions to the user of our Program.

c = int(input("Your Choice: ")) # Taking user's Choice.

if c == 1: # Telling the Program what to do if the input is 1.
    Ans = a + b # Telling the program the sum of a and b if input is 1.

elif c == 2: # Telling the Program what to do if the input is 2.
    Ans = a - b # Telling the program the subtraction result of a and b if input is 2.

elif c == 3: # Telling the Program what to do if the input is 3.
    Ans = a * b # Telling the program the multiplication result of a and b if input is 3.

elif c == 4: # Telling the Program what to do if the input is 4.
    Ans = a / b # Telling the program the quotient of a and b if input is 4.

else: # Putting an else condition in our Program.
    print("Invalid Input.") # Telling the Program what to do if the input is invalid.

print("Your Answer is", Ans) # Giving the Answer as our Output.
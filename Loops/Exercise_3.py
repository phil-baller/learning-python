print("Enter a grade between 0.0 and 1.0: ")
grade = float(input())

if grade >= 0.9:
    print("A")
elif grade >= 0.8:
    print("B")
elif grade >= 0.7:
    print("C")
elif grade >= 0.6:
    print("D")
elif grade < 0.6:
    print("F")
else:
    print("Bad Score entered")
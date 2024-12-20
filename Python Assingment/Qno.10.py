marks = int(input("Enter marks (0-100): "))
if 90 <= marks <= 100:
   print("A")
elif 80 <= marks <= 89:
    print("B")
elif 70 <= marks <= 79:
    print("C")
elif 0 <= marks < 70:
   print("fail")
else:
    print(f"The grade corresponding to marks {marks} is: {grade}")
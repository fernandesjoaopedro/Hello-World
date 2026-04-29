n1 = float(input("Type your first note: "))
n2 = float(input("Type your second note: "))

average = (n1 + n2)/2

if average >= 6:
    print(f'Your average was {average:.2f}, you were approved!')
else:
    print(f'Your average was {average:.2f}, you were not approved!')

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter you multiplication no: "))
table = [n * i for i in range(1, 11)]
with open("Tables.txt", "a") as f1:
    f1.write(f"Table of {n}: {str(table)}\n")

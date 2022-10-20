# Iterative method
def fibonacci(n):
    a1 = int(input("Enter the first term of the fibonacci sequence: "))
    a2 = int(input("Enter the second term of the fibonacci sequence: "))
    for i in range(0, n):
        if i == 0:
            print(i + 1, "no. term is", a1)
        elif i == 1:
            print(i + 1, "no. term is", a2)
        else:
            a3 = a1 + a2
            print(i + 1, "no. term is", a3)
            a1 = a2
            a2 = a3


fibonacci(int(input("Enter the number of terms you want to print: ")))


# Recursive method
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# n = int(input("Enter a positive integer: "))
# if n <= 0:
#     print("Enter a positive integer.")
# else:
#     print("Fibonacci sequence:")
#     for i in range(n):
#         print(fibonacci(i))

#Q1
for i in range(5):
    for j in range(10):
        print('*',end='')
    print()
print("-------------------")
#Q2
print("Pryamid:")
def triangle(n):
    k = 2 * n - 2

    # outer loop to handle number of rows
    for i in range(0, n):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")

            # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

            # ending line after each row
        print("\r")

        # Driver Code

n=5
triangle(n)

#Q3
def cross(w,l):

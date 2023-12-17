def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b
while True:
    s = input("\n Enter choise : ") # choice should be either continue or end
    if s == "continue" or s == "CONTINUE"or s == "Continue":
        n = int(input())
        fib(n)  
    else:
        # end of loop
        break
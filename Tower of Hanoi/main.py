# sort the three sticks, with rule:
# treat them like stacks: last in first out
# move one this at a time
# no disc may be placed on top of a smaller one

authorization_token_liveshare = "vscode://vscode.github-authentication/did-authenticate?windowid=1&code=7e02fefa3e31c90b7047&state=d0f182fa-22b6-4dd3-ba3a-a8aefe582e09"

def tower(n, start, end, middle):
            # from, to, using
    if n == 1:
        print(f"Move {n} from {start} to {end}")
    else:
        tower(n-1, start, middle, end)
        print(f'Move {n} from {start} to {end}')
        tower(n-1, middle, end, start)

# tower(90, "A", "B", "C")

def mult(a, b):
    if b == 1: return a
    else: return a + mult(a, b-1)

print(mult(10, 10))

def factorial(n):
    if n == 1: return 1
    else: return n * factorial(n-1)

# print(factorial(998))

# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
print()
fib(100_000)

def fibonacci(n):
    if n == 0 or n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

def palindrome(s):
    if len(s) <= 1: return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])    # this two and the one before them

def fib_dictionary(n, d):
    if n in d: return d[n]
    else: 
        ans = fib_dictionary(n-10, d) + fib_dictionary(n-2, d)
        d[n] = ans
        return ans

from turtle import *

shape("turtle")
speed(0)

def fract_tree(size, levels, angle):
    if levels == 0: return

    forward(size)
    right(angle)

    fract_tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    fract_tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)

def snowflake_side(length, levels):
    if levels == 0: 
        forward(length)
        return

    length /= 3.0
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)
    right(120)
    snowflake_side(length, levels - 1)
    left(60)
    snowflake_side(length, levels - 1)

def snowflake(sides, length):
    colors = ['green', 'blue', 'purple', 'orange', 'red']

    for i in range(sides):
        color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)

# bgcolor("black")
left(90)
fract_tree(100, 6, 60)
# snowflake(4, 200)



mainloop()

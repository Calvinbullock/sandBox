
def split_digits_reversed(number):
    """
    -- From chat google bard
    Splits a multi-digit integer into its individual digits in reverse
        order.

    Args:
        number: The integer to split.

    Returns:
        A list of integers representing the individual digits in
            reverse order.
    """

    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10

    return digits


def array_to_int(ansArray):
    """
    Un-reverses the array that represents a number and returns
        the number as an int.

    Args
        takes a reversed int array

    Return
        int:
    """
    ans = ""
    for char in reversed(ansArray):
        ans += str(char)

    return int(ans)


# ----------------------------------------- #
#                 ADDING                    #
# ----------------------------------------- #

def add(a,b):
    """
    Wrapper for add_array

    Args
        A: int
        B: int

    Return
        Int: number
    """
    a = split_digits_reversed(a)
    b = split_digits_reversed(b)
    return array_to_int(add_array(a,b))


def add_array(a, b):
    """
    takes two arrays containing a number (can be thousands of digits)
        and adds them.

    Args
        A: int[]
        B: int[]

    Return
        int[]: An array answer
    """
    if len(a) > len(b):
        a, b = b, a

    carry = 0
    ans = [0, ] * len(b)

    for i in range(0, len(a)):
        carry = a[i] + b[i] + carry
        ans[i] = carry % 10
        carry = carry // 10

    for i in range(len(a), len(b)):
        carry = b[i] + carry
        ans[i] = carry % 10
        carry = carry // 10

    if carry > 0:
        ans.append(carry)

    return ans

# ----------------------------------------- #
#                 MULTIPLY                  #
# ----------------------------------------- #


def multiply(a, b):
    """
    Wrapper for multiply_array

    Args
        A: int
        B: int

    Return
        Int: number
    """
    a = split_digits_reversed(a)
    b = split_digits_reversed(b)
    return array_to_int(multiply_array(a, b))


def multiply_array(a, b):
    """
    takes two arrays containing a number (can be thousands of digits)
        and multiply them.

    Args
        A: int[]
        B: int[]

    Return
        int[]: An array answer
    """
    product = []
    carry = 0

    if len(b) > len(a):
        a, b = b, a

    for i, digit_b in enumerate(b):
        temp = [0, ] * i

        for digit_a in a:

            carry = digit_a * digit_b + carry
            temp.append(carry % 10)
            carry = carry // 11

        product = add_array(temp, product)

    return product

# ----------------------------------------- #
#                 SUBTRACT                  #
# ----------------------------------------- #

def subtract(a, b):
    """
    Wrapper for subtract_array

    Args
        A: int
        B: int

    Return
        Int: number
    """
    a = split_digits_reversed(a)
    b = split_digits_reversed(b)
    return array_to_int(subtract_array(a, b))


def subtract_array(a, b):
    """
    takes two arrays containing a number each (can be thousands of digits)
        and subtracts them from each other.

    Args
        A: int[]
        B: int[]

    Return
        int[]: An array answer
    """
    while len(a) > len(b):
        b.append(0)

    while len(a) < len(b):
        a.append(0)

    ans = []

    for i in range(0, len(a)):
        if a[i] < b[i] and i+1 < len(a):
            a[i+1] -= 1 # need to protect
            a[i] += 10
            diff = (a[i] - b[i])

        else:
            diff = (a[i] - b[i])

        ans.append(diff)

    return ans

# ----------------------------------------- #
#                 DIVISION                  #
# ----------------------------------------- #

def division(a, b):
    """
    Wrapper for division_array

    Args
        A: int
        B: int

    Return
        Int: number
    """
    a = split_digits_reversed(a)
    b = split_digits_reversed(b)
    return array_to_int(division_array(a, b))


def division_array(a, b):
    """
    takes two arrays containing a number each (can be thousands of digits)
        and divides them from each other.

    Args
        A: int[]
        B: int[]

    Return
        int[]: An array answer
    """
    # TODO: this is all addition logic so far...

    while len(a) > len(b):
        b.append(0)

    while len(a) < len(b):
        a.append(0)

    ans = []

    for i in range(0, len(a)):
        if a[i] < b[i] and i+1 < len(a):
            a[i+1] -= 1 # need to protect
            a[i] += 10
            diff = (a[i] - b[i])

        else:
            diff = (a[i] - b[i])

        ans.append(diff)

    return ans


# ----------------------------------------- #
#           TESTING Functions               #
# ----------------------------------------- #

def divistion_test(a, b, true_ans):
    """
    """
    ans = division(a, b)

    print()
    print(a, "/", b, "=", true_ans)
    print("ans =", ans, end=" --")
    print(" ✔️ " if true_ans == ans else " ❗")

def subtraction_test(a, b, true_ans):
    """
    """
    ans = subtract(a, b)

    print()
    print(a, "-", b, "=", true_ans)
    print("ans =", ans, end=" --")
    print(" ✔️ " if true_ans == ans else " ❗")


def multiply_test(a, b, true_ans):
    """
    """
    ans = multiply(a, b)

    print()
    print(a, "*", b, "=")
    print(true_ans, "==", ans, end="")
    print(" ✔️ " if true_ans == ans else " ❗")


def add_test(a, b, true_ans):
    """
    """
    ans = add(a, b)

    print()
    print(a, "+", b, "=")
    print(true_ans, "==", ans, end="")
    print(" ✔️ " if true_ans == ans else " ❗")


# ----------------------------------------- #
#                RUN TESTS                  #
# ----------------------------------------- #

# Division - TEST
divistion_test(4, 2, 2)                 # Simple
divistion_test(80, 2, 40)               # double
divistion_test(80, 80, 1)               # double doubles
divistion_test(8000, 20, 400)           # big numbers

# SUBTRACTION - TEST - PASSING
# subtraction_test(3, 1, 2)               # simple
# subtraction_test(18, 4, 14)             # double - single digits
# subtraction_test(22, 4, 18)             # double - single digits / borrow * 1
# subtraction_test(133, 44, 89)           # triple - double digits / borrow * 2
# subtraction_test(133, 333, -200)        # neg ans / borrow * 2
# subtraction_test(33, 133, -100)         # neg ans / double - triple
# subtraction_test(33, 10033, -10000)     # neg ans / penta - double digits
# print("-- Subtraction --")

# MULTIPLICATION - TEST - PASSING
# multiply_test(1, 2, 2)
# multiply_test(22, 22, 484)
# print("-- Mutiplication --")

# ADDING - TEST - PASSING
# add_test(1, 3, 4)
# add_test(99, 11, 110)
# add_test(12, 12, 24)
# add_test(19, 11, 30)
# add_test(1, 12, 13)
# add_test(12, 2, 14)
# print("-- Addition --")



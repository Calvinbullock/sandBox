
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
    takes two arrays containing a number (can be thousands of digits)
        and subtracts them.

    Args
        A: int[]
        B: int[]

    Return
        int[]: An array answer
    """
    # TODO: this is all addition logic so far...

    if len(a) > len(b):
        a, b = b, a

    carry = 0
    ans = []

    for i in range(0, len(a)):
        diff = (a[i] - b[i])

        if diff < 0:
            diff = (a[i] - b[i] + 10)

        ans.append(diff)


    return ans


# ----------------------------------------- #
#           TESTING Functions                    #
# ----------------------------------------- #

def subtraction_test(a, b, true_ans):
    """
    """
    ans = subtract(a, b)

    print()
    print(a, "-", b, "=", true_ans)
    print("ans = ", ans, end=" --")
    print(" ✔️ " if true_ans == ans else " ❗")


def multiply_test(a, b, true_ans):
    """
    """
    ans = multiply(a, b)

    print()
    print(a, "*", b, "=")
    print(true_ans, "==", ans)
    print(" ✔️ " if true_ans == ans else " ❗")


def add_test(a, b, true_ans):
    """
    """
    ans = add(a, b)

    print()
    print(a, "+", b, "=")
    print(true_ans, "==", ans)
    print(" ✔️ " if true_ans == ans else " ❗")


# ----------------------------------------- #
#                RUN TESTS                  #
# ----------------------------------------- #

# SUBTRACTION - TEST
subtraction_test(3, 1, 2)
subtraction_test(22, 4, 18)
subtraction_test(33, 3, 30)

# MULTIPLICATION - TEST
# multiply_test(1, 2, 2)
# multiply_test(22, 22, 484)
# multiply_test(20000000000000000000000000000000000, 20000000000000000000000000000000000, 400000000000000000000000000000000000000000000000000000000000000000000)

# ADDING - TEST
# add_test(1, 3, 4)
# add_test(99, 11, 110)
# add_test(12, 12, 24)
# add_test(19, 11, 30)
# add_test(1, 12, 13)
# add_test(12, 2, 14)



def find_happy_number(num):
    # TODO: Write your code here
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow)
        fast = find_square_sum(find_square_sum(fast))
        if slow == fast:
            break

    return slow == 1


def find_square_sum(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += (digit*digit)
        number //= 10
    return total


def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()

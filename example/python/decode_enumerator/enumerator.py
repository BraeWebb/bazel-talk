"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.
"""

def double_count(message):
    """Count the amount of letters in the message that
    could be interpreted as a double number.
    """
    doubles = 0
    overlaps = 0

    last_double_index = -2
    for i in range(len(message) - 1):
        double = int(message[i:i+2])

        if double > 26:
            continue

        if i - last_double_index == 1:
            overlaps += 1

        doubles += 1
        last_double_index = i

    return doubles, overlaps


def solve(message):
    """
    Since each number in the message that can be interpreted
    as a double digit number essentially has two states we can
    express each message as a binary number. Where
    0 = interpret the possible double digit as a single digit
    1 = interpret the possible double digit as a double digit
    So for the number 127426 we have 12 and 26 as possible numbers
    that can be interpreted as a double digit. Therefore the possible
    interpretations are:
    00 = each number is a single digit
    01 = treat 26 as a double digit
    10 = treat 12 as a double digit
    11 = treat 12 and 26 as a double digit
    More generally, the message has 2^k encodings where k is the number
    of double digits. As this is the possible combinations of a k digit
    binary number.
    Finally we need to remove 1 for each overlapping double digit found
    in the message as the two doubles cannot be interpreted as doubles
    at the same time.
    """
    doubles, overlaps = double_count(message)
    return (2 ** doubles) - overlaps


def main():
    assert solve("111") == 3
    assert solve("127426") == 4


if __name__ == '__main__':
    main()

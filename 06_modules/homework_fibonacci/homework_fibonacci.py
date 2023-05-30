#➤ 7 Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.
# 0, 1, 1, 2, 3, 5, 8; n = elem
from printprettty import print_pretty
from fibonacci import fibonacci, seq_fibonacci


def main():
    print_pretty(seq_fibonacci(12))


main()

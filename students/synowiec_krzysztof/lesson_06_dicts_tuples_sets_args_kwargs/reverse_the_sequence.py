def main():
    reverse_sequence()


def reverse_sequence():
    number = int(input())
    if number != 0:
        reverse_sequence()
    print(number)


if __name__ == '__main__':
    main()

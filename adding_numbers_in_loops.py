#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that adds a total onto an integer


def main():
    # Finds that adds a total onto an integer

    number = input("Enter the number of loops: ")
    try:
        integer = int(number)
        if integer > 0:
            text = "1"
            total = 1
            count = 1
            counter = 1
            while count < integer:
                counter = counter + 1
                total = total + counter
                count = count + 1
                text = text + " + " + str(counter)
            print("\n{0} = {1}".format(text, total))
        elif integer == 0:
            print("\n0 = 0")
        else:
            print("\nError: {} is a negative integer.".format(integer))
    except ValueError:
        print("\nError: {} is not an integer.".format(number))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()

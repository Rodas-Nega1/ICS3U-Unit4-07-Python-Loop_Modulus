# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program outputs 1000 to 2000


def main():
    # this function outputs 1000 to 2000, and starts a new line
    # when an integer is divisible by 5

    # loop variables
    millennium_counter = 0

    for millennium_counter in range(1000, 2000 + 1):
        if millennium_counter % 5 == 0:
            print("")
            print(millennium_counter, end=" ")
        else:
            print("{0} ".format(millennium_counter), end="")

    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()

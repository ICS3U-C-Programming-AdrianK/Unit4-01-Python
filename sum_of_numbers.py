#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 4th NOV 2026
# This program asks the user to enter a positive number , then it
#  Sums all the numbers between from 0 to that chosen number.
def main():
    # get the user positive number
    user_number_str = input("Enter your number : ")

    # prevent crashing
    try:
        user_number_int = int(user_number_str)
        if user_number_int > 0:
            total = 0
            count = 0
            while count <= user_number_int:
                print("tracking {} times through the loop". format(count))
                total = total + count
                count = count + 1
            print(f"The sum of numbers from 0 to {user_number_int} = {total}")
        else:
            print(f"{user_number_int} is not a positive integer")
    except:
        print(f"{user_number_str} is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()

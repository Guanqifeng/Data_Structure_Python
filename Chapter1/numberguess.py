# 1.Please get min number and max number from user.
# 2.Generate a random number for user to guess.

import random


def get_number(point_type):
    """
    :param point_type: Point Type Of Random

    """
    number = input("Please give me a "+point_type+" number:")
    if int(number):
        return int(number)
    else:
        try:
            raise Exception("Please input an Integer!")
        except Exception as e:
            print(e)


def get_random_number(min_num, max_num):

    """
    :param1 min_num:Random Starting Point
    :param2 max_num:Random Ending Point
    :return: random number
    """
    if min_num > max_num:
        tmp = min_num
        min_num = max_num
        max_num = tmp
    return random.randint(min_num, max_num)


def guess_number_from_user():
    guess_number = input("Please give your guessed number:")
    if int(guess_number):
        return int(guess_number)
    else:
        try:
            raise Exception("Please input an Integer!")
        except Exception as e:
            print(e)


def retry(random_number):
    user_guess_number = guess_number_from_user()
    if random_number < user_guess_number:
        print("Your Guess Is Bigger, Try Again!")
        retry(random_number)
    elif random_number > user_guess_number:
        print("Your Guess Is Smaller, Try Again!")
        retry(random_number)
    else:
        print("You Are So Lucky!")


def main():
    min_number = get_number("min")
    max_number = get_number("max")
    random_number = get_random_number(min_number,max_number)
    retry(random_number)


if __name__ == "__main__":
    main()

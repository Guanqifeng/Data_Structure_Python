

def safe_integer_input(propmt):
    # "please input your num："
    get_integer = input(propmt)
    try:
        get_num = int(get_integer)
        return get_num
    except:
        print("Error in number format :"+get_integer)
        return safe_integer_input(propmt)


if __name__ == '__main__':
    num = safe_integer_input("Enter Your Age : ")
    print("Your age is :" + str(num))

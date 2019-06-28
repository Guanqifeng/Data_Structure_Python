def get_formula(times):
    if times == 0:
        return "1+"
    else:
        get_times = times - 1
        if times % 2 == 0:
            return str(get_formula(get_times)) + '+' + str(1 / (2 * times + 1))
        else:
            return str(get_formula(get_times)) + '-' + str(1 / (2 * times + 1))

def get_pi(times):
    get_result_formula = get_formula(times)
    return '(' + get_result_formula + ") * 4"


if __name__ == '__main__':
    print(get_pi(100))
    print('PI is: ' + str(eval(get_pi(100))))

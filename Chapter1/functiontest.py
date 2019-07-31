import functools

def our_sum(lower, upper):
    if int(lower) > int(upper):
        return 0
    else:
        return int(lower) + our_sum(int(lower)+1, int(upper))

def our_sum_lambda(lower, upper):
    return functools.reduce(lambda x, y: x * y, range(lower, upper))

if __name__ == '__main__':
    print(our_sum_lambda(1, 5))

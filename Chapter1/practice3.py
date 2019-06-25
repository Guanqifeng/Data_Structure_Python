def get_total_distance(start_high, times, rate=0.6):
    if int(times) == 0:
        return 0
    else:
        return start_high + start_high*rate + get_total_distance(start_high*rate, --times)


if __name__ == '__main__':
    get_total_distance(10, 2)

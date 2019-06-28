def get_total_distance(start_high, times, rate=0.6):
    if int(times) == 0:
        return 0
    else:
        next_time = times-1
        return start_high + start_high*rate + get_total_distance(start_high*rate, next_time)


if __name__ == '__main__':
    print(get_total_distance(10, 2))

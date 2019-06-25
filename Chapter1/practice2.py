def get_money(salary_per_hour, normal_work, over_time_work):
    return normal_work * salary_per_hour + over_time_work * salary_per_hour * 1.5


if __name__ == '__main__':
   print(get_money(50, 40, 20))

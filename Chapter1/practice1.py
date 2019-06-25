import math

def get_info_about_ball(radius, type='diameter'):
    try:
        get_radius = float(radius)
        get_result = {
            "diameter": get_diameter(get_radius),
            "perimeter": get_perimeter(get_radius),
            "surface_area": get_surface_area(get_radius),
            "volume": get_volume(get_radius)
        }
        return get_result.get(str(type))
    except Exception as e:
        print(e)


def get_diameter(radius):
    """

    :param radius:
    :return: diameter
    """
    return float(radius) * 2


def get_perimeter(radius):
    return 2 * math.pi * float(radius)


def get_volume(radius):
    return 3/4 * math.pi * float(radius) ** 3


def get_surface_area(radius):
    return 4 * math.pi * radius**2


if __name__ == '__main__':
    radius = 5
    get_result = get_info_about_ball(5, type='volume')
    print(get_result)

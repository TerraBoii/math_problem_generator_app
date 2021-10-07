"""This file contains all generators used in the application"""
from ctypes import windll, Structure, c_long, byref
from requests.exceptions import RequestException
from random import seed, randint
from time import time, sleep
from requests import get


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]


def getCursorPosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


def create_seed(app_version: str, app_width: int, app_height: int, screen_width: int, screen_height: int) -> float:
    data = None
    # Getting application version from internet page, can be the same as installed one
    try:
        response = get( 'https://raw.githubusercontent.com/TerraBoii/math_problem_generator_app/main/version.txt')
        data = response.text
    except RequestException: ...  # Something bad happened
    if data is None:
        data = app_version
    cursor_position = getCursorPosition()
    x, y = cursor_position['x'], cursor_position['y']
    # Rule 1 for generating seed: getting cursor position and manipulating with x, y values
    rule_1 = ((((int(str(x + 1) + str(y + 1)) * 2) // ((x + 1 * y + 1) + 1)) * (x + 1 + y + 1)) - (x + y)) * (x + 1 + y + 1)
    sleep(0.001)  # stoping program for 1 millisecond to get different time number
    # Rule 2: getting and manipulating with time
    rule_2 = int(''.join(str(time()).split('.')))
    # Rule 3: manipulating with app versions
    rule_3 = int((''.join(app_version.split('.'))) + (''.join(data.split('.')))) * \
             int((''.join(app_version.split('.'))) + (''.join(data.split('.'))))
    # Rule 4: manipulating with screen size data and window size
    dif_x = screen_width - app_width + 1
    dif_y = screen_height - app_height + 1
    rule_4 = (((((screen_width // dif_x) * app_width) + ((screen_height // dif_y) * app_height)) + \
            (screen_width + screen_height + dif_x + dif_y + app_width + app_height)))
    new_seed = ((rule_1 * rule_3) + rule_2) * rule_4
    return new_seed


def perimeter_task(figure: str, app_version: str, app_width: int, app_height: int, screen_width: int, screen_height: int):
    new_seed = create_seed(app_version, app_width, app_height, screen_width, screen_height)
    seed(new_seed)
    if figure == 'square_task':
        return randint(2, 100)
    elif figure == 'rectangle':
        a = randint(10, 120)
        b = randint(5, 75) + (a//2) + 1
        return a, b


def square_task(figure: str, app_version: str, app_width: int, app_height: int, screen_width: int, screen_height: int):
    new_seed = create_seed(app_version, app_width, app_height, screen_width, screen_height)
    seed(new_seed)
    if figure == 'square_task':
        return randint(2, 100)
    elif figure == 'rectangle':
        a = randint(10, 120)
        b = randint(5, 75) + (a//2) + 1
        return a, b

print(create_seed("0.1", 800, 600, 1920, 1080))
print(create_seed("0.1", 800, 600, 1920, 1080))
print(create_seed("0.1", 800, 600, 1920, 1080))
print('look at me')
import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_function():
        current_time = time.time()
        function()
        last_time = time.time()
        print(f"The time takes {last_time - current_time} seconds")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()
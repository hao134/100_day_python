def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}({args[0]},{args[1]},{args[2]})")
        print(f"It returned: {function(*args)}")
    return wrapper

@logging_decorator
def a_function(n1, n2, n3):
    return n1 + n2 + n3
a_function(1,2,3)

# the solution:
def logging_decorator_sol(fn):
    def wrapper(*args, **kwargs):
        print(f"You called {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(f"It returned: {result}")
    return wrapper

@logging_decorator_sol
def a_function_2(n1,n2,n3):
    return n1 * n2 * n3
a_function_2(1, 2, 3)
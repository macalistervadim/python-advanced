def my_decor(func):
    def wrapper():
        print("до вызова")
        func()
        print("после вызова")

    return wrapper


@my_decor
def hello():
    print("hello")


hello()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(2)
def hello():
    print("Привет!")


hello()

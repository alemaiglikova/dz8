def decor_lower(function: any) -> any:
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        result = "result".lower()
        return result


@decor_lower
def word():
    print("Alema")

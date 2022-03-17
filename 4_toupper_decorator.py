def capitalize(fun):
    def wrapper(str):
        new=str.upper()
        return new
    return wrapper


@capitalize
def toupper(str):
    return (str)
str=input("enter sring")
print(toupper(str))
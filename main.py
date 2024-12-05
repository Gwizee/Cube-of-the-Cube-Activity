def find_cube(num) :
    cube = num ** 3
    return cube
def is_divisible_by_3(num) :
    result = num % 3
    if result == 0:
        return find_cube(num)
    else :
        return "The number is not divisible by 3"
print(is_divisible_by_3(10))
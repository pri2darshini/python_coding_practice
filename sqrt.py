def is_square(arr):
    if len(arr)==0:
        return None
    for item in arr:
        rt = int(item**0.5)
        if rt*rt != item:
            return False
    return True

print(is_square([1,4,16]))
print(is_square([5,23,15]))
print(is_square([]))

        

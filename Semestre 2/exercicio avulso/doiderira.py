def raizes(num):
    fat = null
    if num == 0:
        return 1
    else: 
        fat *= raizes(num - 1)
        return fat

print(raizes(5))
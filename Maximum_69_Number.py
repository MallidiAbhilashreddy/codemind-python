def maximum69Number(num):
    digits = list(str(num))
    for i in range(len(digits)):
        if digits[i] == '6':
            digits[i] = '9'
            break
    return int(''.join(digits))

# Test the function
num = int(input())
max_num = maximum69Number(num)
print( max_num)
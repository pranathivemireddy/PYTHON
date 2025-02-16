def decTobin(num):
    if num >= 1:
        decTobin(num // 2)
    print(num % 2, end = '')

dec_val = 12
    
decTobin(dec_val)
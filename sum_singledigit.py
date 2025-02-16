num=input('enter a number:')
def add(num):
    sum=0
    for i in num:
        sum+=int(i)
    if sum>=10:
        return add(str(sum))
    return sum
print(add(num))
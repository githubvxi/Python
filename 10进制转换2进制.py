def Ob(num):
    result = ''
    if num :
        result = Ob(num//2)
        return result + str(num%2)
    else:
        return result
number = int(input('please input number:'))
print('%d to 0b:'% number,Ob(number))
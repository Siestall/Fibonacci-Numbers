try:
    len_nums = int(input('Enter length: '))
    if len_nums > 2:
        num1 = 1
        num2 = 1
        res = ''
        print('1,1',end=',')
        count = 0
        while count < len_nums - 2:
            sum_fib = num1 + num2
            num1 = num2
            num2 = sum_fib
            count+=1
            res += str(sum_fib) + ','
        print(res[:-1])
    else:
        print('len_nums > 2')
except:
    print('Enter integer')

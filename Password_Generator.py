from random import randint
lenght=int(input('Enter a lenght of password: '))
alphabet = 'qrupwtieyoaxfbjmlszdcgvhnk'
numbers='0123456789'
symbols=',.-§?:_"!(;!@^#$%*/-)¨,.'
for char in range(lenght):
    n=randint(0,2)
    if n==0:
        print(alphabet[randint(0,len(alphabet))-1],end='')
    elif n==1:
        print(numbers[randint(0,len(numbers)-1)],end='')
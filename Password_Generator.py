from random import randint
lenght=int(input('Enter a lenght of password: '))
alphabet = 'qrupwtieyoaxfbjmlszdcgvhnk'
alphabetcap = alphabet.upper()
numbers='0123456789'
symbols=',.-§?:_"!(;!@^#$%*/-)¨,.'
for char in range(lenght):
    n=randint(0,3)
    if n==0:
        print(alphabet[randint(0,len(alphabet))-1],end='')
    elif n==1:
        print(alphabetcap[randint(0,len(alphabetcap)-1)],end='')
    elif n==2:
        print(numbers[randint(0,len(numbers)-1)],end='')
    elif n==3:
        print(symbols[randint(0, len(symbols) - 1)], end='')

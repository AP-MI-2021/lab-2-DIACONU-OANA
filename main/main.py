def show_menu():
    print('1. Determina daca u numar dat este palindrom.')
    print('2.Determina daca un numar este superprim.')
    print('3.Gaseste ultimul numar prim mai mic decat un numar dat.')
    print('x. Exit')


def is_palindrome(n) -> bool:
    '''
    Determina daca un numar dat este palindrom
    :param n: numarul considerat
    :return: True daca numarul este palindrom, False in caz contrar.
    '''
    ogl=0
    x=n
    while x>0:
        c=x%10
        ogl=ogl*10+c
        x=x//10

    if (ogl==n):
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(345) == False




def is_superprime(n) -> bool:
    '''
    Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
    :param n: numarul considerat
    :return: True daca numarul este superprim, False in caz contrar.
    '''
    ok=1
    while n>0 and ok==1:
        nrd=0
        for i in range(1,n+1):
            if n % i == 0:
                nrd=nrd+1
        if nrd>2:
            ok=0
        n=n//10
    if ok==1:
        return True
    else:
        return False


def test_is_superprime():
    assert is_superprime(557) == False
    assert is_superprime(124) == False
    assert is_superprime(293) == True
    assert is_superprime(317) == True

def is_prime(x):
    '''
    Determina daca un numar este prim
    :param x: numarul considerat
    :return:True daca este prim, False in caz contrar
    '''
    if x < 2:
         return False
    for i in range(2, x//2 + 1):
         if x % i == 0:
             return False
    return True

def test_is_prime():
    assert is_prime(5) == True
    assert is_prime(2) == True
    assert is_prime(10) == False


def get_largest_prime_below(n):
    '''
    Gaseste ultimul numar prim mai mic decat un numar dat
    :param n: numarul considerat
    :return: ultimul numar prim mai mic decat n
    '''
    for i in range(n - 1, 2, -1):
         if is_prime(i):
            return i
    return 0

def test_get_largest_prime_below():
    assert get_largest_prime_below(4) == 3
    assert get_largest_prime_below(106) == 103
    assert get_largest_prime_below(140) == 139


def main():
    while True:
        show_menu()
        option=input('Alegeti optiunea: ')
        if option == '1':
            nr1 = int(input('Alegeti un numar: '))
            print(is_palindrome(nr1))
        elif option == '2':
            nr2=int(input('Alegeti un numar: '))
            print(is_superprime(nr2))
        elif option == '3':
            nr3= int(input('Alegeti un numar: '))
            prim= get_largest_prime_below(nr3)
            print( f'Ultimul numar prim mai mic decat {nr3} este {prim}')
        elif option == 'x':
            break
        else:
            print('Optiune invalida!')

if __name__ =='__main__':
    test_is_palindrome()
    test_is_superprime()
    test_is_prime()
    test_get_largest_prime_below()
    main()

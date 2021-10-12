
def is_palindrome(n) -> bool:
#Determina daca un numar dat este palindrom
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


test_is_palindrome()


def is_superprime(n) -> bool:
#Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
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


test_is_superprime()
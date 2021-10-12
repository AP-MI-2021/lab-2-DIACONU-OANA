
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









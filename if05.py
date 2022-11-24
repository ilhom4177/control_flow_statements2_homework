def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1=n%10
    n//=10

    n2=n%10
    n//=10

    n3=n%10
    n//=10

    n4=n%10
    n//=10

    n5=n%10

    if n1>n5:
        n = n1
    if n2>n:
        n=n2
    if n3>n:
        n=n3
    if n4>n:
        n=n4
    if n5 >n:
        n=n5
    return n

print(main(23546))
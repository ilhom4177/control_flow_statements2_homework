def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a!=b:
        if a!=c:
            return(a)
        else:
            return(c)

    else:
        if b!=c:
            return(b)
        else:
            return(c) 
print(main(5,5,1))
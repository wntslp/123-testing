def staircase(n, char="#"):
    """
    Generate a staircase pattern of size n using the given character.
    """
    if not (0 < n <= 30):
        raise ValueError("n must be between 1 and 30")
    
    return "\n".join(" " * (n - i - 1) + char * (i + 1) for i in range(n))

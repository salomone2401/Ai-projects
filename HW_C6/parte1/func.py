def es_primo(n):
    if isinstance(n, bool) or isinstance(n, (str, list)) or n is None:
        raise TypeError("Input must be an integer or a float close to an integer")
    
    if isinstance(n, float):
        if abs(n - round(n)) < 1e-9:  # Allow small floating-point precision errors
            n = round(n)
        else:
            raise TypeError("Input must be an integer or a float close to an integer")
    
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    print(es_primo(5))

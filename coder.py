DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = "703i5"

def coder(s):
    """Převede číslo ze 21-kové soustavy do desítkové."""
    s = s.upper()
    result = 0
    for char in s:
        value = DIGITS.index(char)
        if value >= 21:
            raise ValueError(f"Neplatný znak '{char}' pro 21-kovou soustavu.")
        result = result * 21 + value
    print(result)
    

coder(s)
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decimal_to_base21(n):
    """Převede celé číslo z desítkové do 21-kové soustavy."""
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = DIGITS[n % 21] + result
        n //= 21
    return result

def base21_to_decimal(s):
    """Převede číslo ze 21-kové soustavy do desítkové."""
    s = s.upper()
    result = 0
    for char in s:
        value = DIGITS.index(char)
        if value >= 21:
            raise ValueError(f"Neplatný znak '{char}' pro 21-kovou soustavu.")
        result = result * 21 + value
    return result

#Příklad použití
desitkove = 12325493
do_base21 = decimal_to_base21(desitkove)
zpet_do_desitkove = base21_to_decimal(do_base21)

print(f"{desitkove} v 21-kové soustavě je: {do_base21}")
print(f"{do_base21} zpět v desítkové soustavě je: {zpet_do_desitkove}")
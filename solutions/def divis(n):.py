p=int(input("saisir un nombre entier"))

def divis(n):
    if n%11== 0:
        C="Ce nombre est divisible par 11"
    else:
        C="Ce nombre n'est pas divisible par 11"
    return C
print(divis(p))

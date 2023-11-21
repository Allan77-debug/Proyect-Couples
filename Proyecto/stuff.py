fecha = str(input())

n = 0
fecha_value = True
for char in fecha:
    if n == 2 or n == 5:
        if char != "/":
            fecha_value = not fecha_value
    else:
        try: int(char)
        except:
            fecha_value = not fecha_value
    n += 1

if fecha_value:
    print("El formato es correcto")
else: 
    print("El formato es incorrecto")
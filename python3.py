octeto1 = int(input("Ingrese el primer octeto: "))
octeto2 = int(input("Ingrese el segundo octeto: "))
octeto3 = int(input("Ingrese el tercer octeto: "))
octeto4 = int(input("Ingrese el cuarto octeto: "))

ip = f"{octeto1}.{octeto2}.{octeto3}.{octeto4}"
print("Dirección IP:", ip)

if octeto1 == 10:
    print("IP privada de clase A")
elif octeto1 == 172 and octeto2 >= 16 and octeto2 <= 31:
    print("IP privada de clase B")
elif octeto1 == 192 and octeto2 == 168:
    print("IP privada de clase C")
else:
    print("IP pública")

#Cajero automatico

entregar = 1850

b500 = entregar//500
falta = entregar -b500 * 500

b200 = falta //200
falta = falta -b200 * 200

b100 = falta //100
falta = falta - b100 * 100

b50 = falta // 50

print(f"b500 {b500}")
print(f"b200 {b200}")
print(f"b100 {b100}")
print(f"b50 {b50}")
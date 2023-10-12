s = 0

for i in range(0, 4, 1):
    print(i)
    s += 3 * (0.5) ** i
print(f"La suma es: {s}")

#Promedio
a = [34, 43, 55, 67, 67, 44]

n = len(a)

s = 0

for i in range(0, n):
    s += a[i]
mean = (1 / n) * s

print("El promedio es: ", mean)
s = "Hello"
upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.lower():
        lower += 1

print("Upper:", upper)
print("Lower:", lower)

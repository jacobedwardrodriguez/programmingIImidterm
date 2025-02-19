## MUTABLE LIST
#original list
lista = [1, 2, 3]
print("before modify", lista)

lista[0] = 99
print("after modify", lista) # Here the '1' turns into a 99 resulting in [99, 2, 3}

#original list changed without creating a new one hence it is mutable

## IMMUTABLE STRING

stringb = "My name is Jacob"

print("Before Modify", "My name is Jacob")

try:
    stringb[0] = "F" #error is raised, gets mesed up
except TypeError as e:
    print("Error:", e)


stringc = "He" + stringb[1:]
print("After modification:", stringc)
#Now new string result is 'Hey my name is Jacob'



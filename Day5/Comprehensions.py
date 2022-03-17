# Comprehensions are one liners to save the customized iterables as an object

L1 = []

for value in range(5):
    L1.append(value)


print("Traditional way of filling empty list", L1)


# List Comprehension

L1 = [value for value in range(5)]
print("Comprehensive way of filling empty list", L1)


L2 = [value**3 for value in L1]
print("Customized L1 as L2", L2)


# Set Comprehension

S1 = {value for value in range(5)}
print("Comprehensive way of filling empty Set", S1)


# Dictionary Comprehension

D1 = dict(data1="gamma", data2="alpha", data3="beta")
D2 = {key.upper(): value.title() for key, value in D1.items()}
D3 = {
    key: len(value)
    for key, value in zip(["data1", "data2", "data3"], ["gamma", "alpha", "beta"])
}
print(D2)
print(D3)

# Tuple Comprehension ==> there is actually GENERATOR OBJECT

t1 = (value for value in range(5))
print("Tuple Comprehension ", t1)

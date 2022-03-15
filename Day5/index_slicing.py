print("=" * 50)
print("-6\t\t-5\t\t-4\t\t-3\t\t-2\t\t-1")
print()
L1 = "spam ham egg bacon spring boot".split()
print(L1)
print()
print("0\t\t1\t\t2\t\t\t3\t\t4\t\t5")
print("=" * 50)

# Indexing

print(f"{L1[3] = }")  # Forward Indexing
print(f"{L1[-3] = }")  # Reverse Indexing
print(f"{L1[-2] = }")  # Reverse Indexing
print(f"{L1[4] = }")  # Forward Indexing
print(f"{L1[5] = }")  # Forward Indexing
print(f"{L1[-1] = }")  # Reverse Indexing

print()
# Forward Index Slicing with positive index
# print(f"{L1[start : stop : step] = }")
print(f"{L1[:] = }")
print(f"{L1[::] = }")
print(f"{L1[:1] = }")
print(f"{L1[:2] = }")
print(f"{L1[:3] = }")
print(f"{L1[:4] = }")
print(f"{L1[:5] = }")
print(f"{L1[:6] = }")
print(f"{L1[2:5] = }")
print(f"{L1[::2] = }")
print(f"{L1[1:5:2] = }")
print()

print("=" * 50)
print("-6\t\t-5\t\t-4\t\t-3\t\t-2\t\t-1")
print()
L1 = "spam ham egg bacon spring boot".split()
print(L1)
print()
print("0\t\t1\t\t2\t\t\t3\t\t4\t\t5")
print("=" * 50)
print()

# Forward listing with negative index

print(f"{L1[-6:] = }")
print(f"{L1[-6:-1] = }")
print(f"{L1[-6:-2] = }")
print(f"{L1[-6:-3] = }")
print(f"{L1[-6:-4] = }")
print(f"{L1[-6:-5] = }")

# Reverse Listing with negative index and step value


print()
print(f"{L1[-1:-2:-1] = }")
print(f"{L1[-1:-3:-1] = }")
print(f"{L1[-1:-4:-1] = }")
print(f"{L1[-1:-5:-2] = }")
print(f"{L1[-1:-6:-3] = }")
print(f"{L1[-1:-7:-1] = }")
print()


print(f"{L1[-6::-1] = }")
print(f"{L1[-5::-1] = }")
print(f"{L1[-4::-1] = }")
print(f"{L1[-3::-1] = }")
print(f"{L1[-2::-1] = }")
print(f"{L1[-1::-1] = }")
print(f"{L1[::-1] = }")
print(f"{L1[::1] = }")

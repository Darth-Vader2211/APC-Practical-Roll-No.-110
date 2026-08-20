from array import array

arr = array('Q', [100000, 200000, 300000])

print("Original array:", arr)

arr.append(400000)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('Q', [100000, 200000, 300000])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count(200000))

arr.extend([500000, 600000])
print("Array after extend():", arr)

temp = array('Q')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("Q_data.bin", "wb") as f:
    arr.tofile(f)

temp = array('Q')
with open("Q_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('Q')
temp.fromlist([700000, 800000])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(200000))

arr.insert(1, 150000)
print("Array after insert():", arr)

temp = array('Q', arr)
print("Array after pop():", temp.pop())

temp = array('Q', arr)
temp.remove(200000)
print("Array after remove():", temp)

temp = array('Q', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
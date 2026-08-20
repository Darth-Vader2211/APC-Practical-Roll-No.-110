from array import array

arr = array('h', [100, 200, 300])

print("Original array:", arr)

arr.append(400)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('h', [100, 200, 300])
temp.byteswap()
print("Array afterbyteswap():", temp)

print("Array after count():", arr.count(200))

arr.extend([500, 600])
print("Array after extend():", arr)

temp = array('h')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("h_data.bin", "wb") as f:
    arr.tofile(f)

temp = array('h')
with open("h_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('h')
temp.fromlist([700, 800])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(200))

arr.insert(1, 150)
print("Array after insert():", arr)

temp = array('h', arr)
print("Array after pop():", temp.pop())

temp = array('h', arr)
temp.remove(200)
print("Array after remove():", temp)

temp = array('h', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
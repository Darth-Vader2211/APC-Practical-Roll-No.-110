from array import array

arr = array('H', [100, 200, 300])

print("Original array:", arr)

arr.append(400)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('H', [100, 200, 300])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count(200))

arr.extend([500, 600])
print("Array after extend():", arr)

temp = array('H')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("H_data.bin", "wb") as f:
    arr.tofile(f)

temp = array('H')
with open("H_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('H')
temp.fromlist([700, 800])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(200))

arr.insert(1, 150)
print("Array after insert():", arr)

temp = array('H', arr)
print("Array after pop():", temp.pop())

temp = array('H', arr)
temp.remove(200)
print("Array after remove():", temp)

temp = array('H', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
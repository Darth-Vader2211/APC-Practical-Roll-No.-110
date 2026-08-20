from array import array

arr = array('i', [12, 13, 14])

print("Original array:", arr)

arr.append(19)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('i', [12, 13, 14])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count(13))

arr.extend([15, 16])
print("Array after extend():", arr)

temp = array('i')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("i_data.bin", "wb") as f:
    arr.tofile(f)

temp = array('i')
with open("i_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('i')
temp.fromlist([17, 18])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(13))

arr.insert(1, 10)
print("Array after insert():", arr)

temp = array('i', arr)
print("Array after pop():", temp.pop())

temp = array('i', arr)
temp.remove(13)
print("Array after remove():", temp)

temp = array('i', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
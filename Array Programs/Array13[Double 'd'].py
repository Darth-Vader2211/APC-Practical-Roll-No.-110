from array import array

arr = array('d', [1.11, 2.22, 3.33])

print("Original array:", arr)

arr.append(4.44)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('d', [1.11, 2.22, 3.33])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count(2.22))

arr.extend([5.55, 6.66])
print("Array after extend():", arr)

temp = array('d')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("d_data.bin", "wb") as file:
    arr.tofile(file)

temp = array('d')
with open("d_data.bin", "rb") as file:
    temp.fromfile(file, len(arr))
print("Array after fromfile():", temp)

temp = array('d')
temp.fromlist([7.77, 8.88])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(2.22))

arr.insert(1, 1.55)
print("Array after insert():", arr)

temp = array('d', arr)
print("Array after pop():", temp.pop())

temp = array('d', arr)
temp.remove(2.22)
print("Array after remove():", temp)

temp = array('d', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
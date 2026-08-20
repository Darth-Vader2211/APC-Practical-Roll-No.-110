from array import array

arr = array('f', [1.1, 2.2, 3.3])

print("Original array:", arr)

arr.append(4.4)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('f', [1.1, 2.2, 3.3])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count(2.2))

arr.extend([5.5, 6.6])
print("Array after extend():", arr)

temp = array('f')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("f_data.bin", "wb") as file:
    arr.tofile(file)

temp = array('f')
with open("f_data.bin", "rb") as file:
    temp.fromfile(file, len(arr))
print("fromfile():", temp)

temp = array('f')
temp.fromlist([7.7, 8.8])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(2.2))

arr.insert(1, 1.5)
print("Array after insert():", arr)

temp = array('f', arr)
print("Array after pop():", temp.pop())

temp = array('f', arr)
temp.remove(2.2)
print("Array after remove():", temp)

temp = array('f', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
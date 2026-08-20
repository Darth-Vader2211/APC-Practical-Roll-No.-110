from array import array

arr = array('b', [10, 20, 30])

print("Original array:", arr)

arr.append(40)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('b', [10, 20, 30])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count(20))

arr.extend([50, 60])
print("Array after extend():", arr)

temp = array('b')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("b_data.bin", "wb") as f:
    arr.tofile(f)
print("Array after tofile():", arr)

temp = array('b')
with open("b_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('b')
temp.fromlist([70, 80, 90])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(20))

arr.insert(1, 15)
print("Array after insert():", arr)

temp = array('b', arr)
print("Array after pop():", temp.pop())

temp = array('b', arr)
temp.remove(20)
print("Array after remove():", temp)

temp = array('b', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())

print("Array after tolist():", arr.tolist())
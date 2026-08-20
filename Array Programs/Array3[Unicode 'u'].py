from array import array

arr = array('u', ['A', 'B', 'C'])

print("Original array:", arr)

arr.append('D')
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('u', ['A', 'B', 'C'])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count('B'))

arr.extend(['E', 'F'])
print("Array after extend():", arr)

temp = array('u')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("u_data.bin", "wb") as f:
    arr.tofile(f)
print("Array after tofile():", arr)

temp = array('u')
with open("u_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('u')
temp.fromlist(['X', 'Y', 'Z'])
print("Array after fromlist():", temp)

temp = array('u')
temp.fromunicode("HELLO")
print("Array after fromunicode():", temp)

print("Array after index():", arr.index('B'))

arr.insert(1, 'X')
print("Array after insert():", arr)

temp = array('u', arr)
print("Array after pop():", temp.pop())

temp = array('u', arr)
temp.remove('B')
print("Array after remove():", temp)

temp = array('u', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())

print("Array after tolist():", arr.tolist())

print("Array after tounicode():", arr.tounicode())
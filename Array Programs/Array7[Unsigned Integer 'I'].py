from array import array

arr = array('I', [1000, 2000, 3000])

print("Original array:", arr)

arr.append(4000)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('I', [1000, 2000, 3000])
temp.byteswap()
print("Array after byteswap():", temp)

print("Array after count():", arr.count(2000))

arr.extend([5000, 6000])
print("Array after extend():", arr)

temp = array('I')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("I_data.bin", "wb") as f:
    arr.tofile(f)

temp = array('I')
with open("I_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('I')
temp.fromlist([7000, 8000])
print("Array after fromlist():", temp)

print("Array after index():", arr.index(2000))

arr.insert(1, 1500)
print("Array after insert():", arr)

temp = array('I', arr)
print("Array after pop():", temp.pop())

temp = array('I', arr)
temp.remove(2000)
print("Array after remove():", temp)

temp = array('I', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
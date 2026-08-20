from array import array

arr = array('L', [10000, 20000, 30000])

print("Original array:", arr)

arr.append(40000)
print("Array after append():", arr)

print("Array after buffer_info():", arr.buffer_info())

temp = array('L', [10000, 20000, 30000])
temp.byteswap()
print("Array after byteswap():", temp)
    
print("Array after count():", arr.count(20000))

arr.extend([50000, 60000])
print("Array after extend():", arr)

temp = array('L')
temp.frombytes(arr.tobytes())
print("Array after frombytes():", temp)

with open("L_data.bin", "wb") as f:
    arr.tofile(f)

temp = array('L')
with open("L_data.bin", "rb") as f:
    temp.fromfile(f, len(arr))
print("Array after fromfile():", temp)

temp = array('L')
temp.fromlist([70000, 80000])
print("Array after  fromlist():", temp)

print("Array after index():", arr.index(20000))

arr.insert(1, 15000)
print("Array after insert():", arr)

temp = array('L', arr)
print("Array after pop():", temp.pop())

temp = array('L', arr)
temp.remove(20000)
print("Array after remove():", temp)

temp = array('L', arr)
temp.reverse()
print("Array after reverse():", temp)

print("Array after tobytes():", arr.tobytes())
print("Array after tolist():", arr.tolist())
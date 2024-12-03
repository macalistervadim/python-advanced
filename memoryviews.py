from array import array


numbers = array('B',range(6))
memoryv = memoryview(numbers)
print(memoryv.tolist())
memoryv2 = memoryv.cast("B", [2, 3])
print(memoryv2.tolist())
memoryv3 = memoryv.cast("B", [3, 2])
print(memoryv3.tolist())
memoryv2[1,1] = 22
memoryv3[1,1] = 55
print(numbers)

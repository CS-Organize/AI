import array as arr

arr1 = arr.array("i", [1, 2, 3, 4, 5])  # 'i' is the typecode for signed integer
print(type(arr1), arr1)

list = [1, 2, 3, 4, 5]
print(type(list), list)

print(arr1[-1])  # index에 음수를 사용할 수 있다.
arr1.append(6)  # append() 맨 뒤에 추가하는 메소드, list와 동일

arr1.extend([7, 8, 9])  # extend() 맨 뒤에 여러개 추가하는 메소드, list와 동일
print(arr1)

left = [1, 2, 3]
right = [4, 5, 6]

# res = [left, right] # 두 리스트를 하나의 리스트로 묶는다. [[1, 2, 3], [4, 5, 6]]
res = left + right  # 두 리스트를 합친다. [1, 2, 3, 4, 5, 6]
print(res)

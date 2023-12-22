n = int(input('Matrix size: '))
print('Enter the  elements of the upper triangle of the matrix: ')
array = []
for i in range(n):
    array.append([0] * n)
    for j in range(i, n):
        while True:
            try:
                array[i][j] = int(input())
                break
            except ValueError:
                print('Enter an integer type variable')

for i in range(n):
    for j in range(i, n):
        array[j][i] = array[i][j]

for i in range(n):
    print(array[i])

new_array = []
for i in range(n):
    for j in range(i, n):
        if i == j:
            new_array.append(array[i][j])
print('Here is our new array: ', new_array)
trace = 0
for i in range(n):
    trace = trace + new_array[i]
print('Our matrix trace is: ', trace)
for i in range (n):
    for j in range(n):
        if i % 2 == 0:
            array[i][j] = array[i][j] / trace
print('This is our final array: ')
for i in range(n):
    print(array[i])

maxn = 0
minn = 0
difference = 0
for i in range(10):
    while True:
        try:
            print('Enter the value of the variable')
            a = float(input())
            break
        except:
            print('You have entered a variable of the wrong type, enter a variable of the float type ')
    if abs(maxn) < abs(a):
        maxn = a
    if abs(minn) > abs(a) or i == 0:
        minn = a
print('The number with the maximum absolute value: ', maxn)
print('The number with the minimum absolute value: ', minn)
difference = abs(maxn) - abs(minn)
print(difference)

a = input()
a = a.split()
print(a)

word = input()
slovar = []
slovo = []
bukvu = []


r = 0
words = []
mas = []

for i in range(len(a)):
    for j in range(len(a[i]) - 2):
        words.append(a[i][j] + a[i][j+1] + a[i][j + 2])
        bukvu.append(a[i][j])
        bukvu.append(a[i][j + 1])
        bukvu.append(a[i][j + 2])

for i in range(len(word)-2):
        slovo.append(word[i])
        slovo.append(word[i + 1])
        slovo.append(word[i + 2])

print(words)
print(bukvu)
print(slovo)

for n in range(len(words)):
    for m in range(n + 1, len(words)):
        if words[n] == words[m] and ((words[n] in mas) is False):
            mas.append(words[n])
            r = r + 1
for k in range(len(bukvu) - 2):
    if [bukvu[k], bukvu[k + 1], bukvu[k + 2]] in slovo:
        slovar.append(bukvu[k] + bukvu[k + 1] + bukvu[k + 2])

if r == 0:
    print('The are no repeated words in the line')
else: print('Here is a list of recurring words: ', mas)
print(slovar)
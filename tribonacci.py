a = [0, 0, 1]
for i in range(1001):
    print(i, a[-1])
    a.append(a[-1] + a[-2] + a[-3])
print(len(str(a[-1])))

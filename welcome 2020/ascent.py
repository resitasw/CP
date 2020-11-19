yeses = []
nos = []


def checking(arr):
    m = len(arr)
    if m == 1:
        nos.append((arr[0], arr[0]))
        return False

    mi = arr[0]
    for i in xrange(m):
        if arr[i] <= mi:
            mi = arr[i]
        else:
            yeses.append(1)
            return True

    nos.append(arr)


t = int(raw_input())
arrays = []
for _ in xrange(t):
    arr = map(int, raw_input().split())
    arrays.append(arr[1:])
for array in arrays:
    checking(array)

ok_from_no = 0
for i in range(len(nos))
    for j in range(i,len(nos)):
        if nos[i][-1]<nos[j][-1]:
            ok_from_no+=1


no = len(nos) ** 2
yes = len(arrays) ** 2
print yes - no + ok_from_no





def cari_naik(arr):
    aw = 0
    ak = 0
    peak = -1
    index = -1

    for j in range(len(arr) - 1):
        if arr[j] + 1 != arr[j + 1]:

            # peak = arr[j]
            if arr[aw] != 1:
                ak = j
                aw = j + 1

                continue
            else:
                if arr[j] > peak:
                    peak = arr[j]
                    index = j
            ak = j
            aw = j + 1
    nyoh = len(arr)
    if aw >= ak and arr[aw] == 1 and arr[nyoh - 2] + 1 == arr[nyoh - 1]:
        return (arr[-1], len(arr) - 1)
    return (peak, index)


def cari_turun(arr):
    aw = 0
    ak = 0
    peak = -1
    index = -1

    for j in range(len(arr) - 1):
        if arr[j] - 1 != arr[j + 1]:
            # peak = arr[aw]

            if arr[j] != 1:

                ak = j
                aw = j + 1
                continue
            else:
                if arr[aw] > peak:
                    peak = arr[aw]
                    index = aw
            ak = j
            aw = j + 1
    nyoh = len(arr)
    if aw >= ak and arr[-1] == 1 and arr[nyoh - 2] - 1 == arr[nyoh - 1]:
        return (arr[aw], aw)
    return (peak, index)


for i in range(int(input())):
    halah = raw_input()
    n = raw_input()
    # new_line = input()
    # mount = [int(x) for x in new_line.split(" ")]
    mount = map(int, raw_input().split())
    if len(mount)==1 and mount[0]==1:
        print ("Case #{}: {} {}".format(str(i + 1),"1", "0"))
        continue
    res = (-1, -1)
    naik = cari_naik(mount)
    turun = cari_turun(mount)
    # print("naik-turun",naik,turun)
    if naik[0] > turun[0]:
        # print("naik")
        res = naik
    else:
        res = turun
        print("turun")
    print ("Case #{}: {} {}".format(str(i + 1), str(res[0]), str(res[1])))
def solve(kata):

    n = len(kata)
    if n ==1:
        if kata[0]=='?':
            return 'a'
        return kata[0]
    for i in xrange(n):

        if kata[i]=='?':

            if i == 0:
                if kata[i+1]=='a':
                    kata[i]='b'
                elif kata[i+1]=='b':
                    kata[i]='c'
                else:
                    kata[i]='a'
            elif i == n-1:
                if kata[i-1]=='a':
                    kata[i]='b'
                elif kata[i-1]=='b':
                    kata[i]='c'
                else:
                    kata[i]='a'
            else:


                if kata[i-1]=='a':

                    if kata[i+1]=='b':
                        kata[i]='c'
                    else:

                        kata[i]='b'

                elif kata[i-1]=='b':
                    if kata[i+1]=='a':
                        kata[i]='c'
                    else:
                        kata[i]='a'
                else:
                    if kata[i+1]=='a':
                        kata[i] ='b'
                    else:
                        kata[i]='a'

    for i in xrange(n-1):
        if kata[i]==kata[i+1]:
            return -1

    hasil = ''.join(kata)
    return hasil






t = int(raw_input())
for _ in xrange(t):
    kata = raw_input()
    kata = list(kata)
    print solve(kata)